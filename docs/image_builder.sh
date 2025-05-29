#!/bin/bash

read -p "Enter Docker image to pull (e.g., nginx:latest): " DOCKER_IMAGE
read -p "Enter the name of your EC2 key pair (do not include .pem): " KEY_NAME

AMI_ID="ami-0e58b56aa4d64231b"  # This may need to be updated in the future
INSTANCE_TYPE="t2.micro"
SECURITY_GROUP_NAME="ec2-docker-sg"
INSTANCE_PROFILE_NAME="EC2InstanceECRAccessProfile"
REGION="us-east-1"
VOLUME_SIZE=20
KEY_FILE="${KEY_NAME}.pem"
ECR_REPO_NAME=$(echo "$DOCKER_IMAGE" | cut -d'/' -f3-)

echo "New ECR repo: '${ECR_REPO_NAME}' to be created in your account."

echo "Looking up VPC ID..."
VPC_ID=$(aws ec2 describe-vpcs \
  --query "Vpcs[0].VpcId" \
  --region "$REGION" \
  --output text)

SUBNET_IDS=($(aws ec2 describe-subnets \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query "Subnets[*].SubnetId" \
  --region "$REGION" \
  --output text))

RANDOM_SUBNET=${SUBNET_IDS[$RANDOM % ${#SUBNET_IDS[@]}]}

echo "Randomly selected Subnet ID: $RANDOM_SUBNET"

echo "Creating security group..."

CREATE_OUTPUT=$(aws ec2 create-security-group \
  --group-name "$SECURITY_GROUP_NAME" \
  --description "Allow SSH and internet access" \
  --region "$REGION" \
  --vpc-id "$VPC_ID" \
  --output text --query 'GroupId' 2>&1)

if [[ $? -ne 0 ]]; then
  if [[ "$CREATE_OUTPUT" == *"InvalidGroup.Duplicate"* ]]; then
    echo "Security group '$SECURITY_GROUP_NAME' already created."
		          
	# Optionally retrieve the existing group ID
		SECURITY_GROUP_ID=$(aws ec2 describe-security-groups \
	 	--region "$REGION" \
		--filters Name=group-name,Values="$SECURITY_GROUP_NAME" \
		--query 'SecurityGroups[0].GroupId' \
		--output text)
	else
	 	echo "Failed to create security group: $CREATE_OUTPUT"
		exit 1
	fi
else
	SECURITY_GROUP_ID="$CREATE_OUTPUT"
	echo "Security group created with ID: $SECURITY_GROUP_ID"
fi                                             

echo "SECURITY_GROUP_ID: $SECURITY_GROUP_ID"

MAX_RETRIES=5
RETRY_DELAY=5 # seconds
ATTEMPT=1

echo "Authorizing security group ingress (SSH on port 22)..."

while [[ $ATTEMPT -le $MAX_RETRIES ]]; do
	OUTPUT=$(aws ec2 authorize-security-group-ingress \
		--group-id "$SECURITY_GROUP_ID" \
		--protocol tcp --port 22 --cidr 0.0.0.0/0 2>&1)
	if [[ $? -eq 0 ]]; then
		echo "Ingress rule added successfully."
		break
	elif echo "$OUTPUT" | grep -q "InvalidPermission.Duplicate"; then
		echo "Ingress rule already exists. Skipping."
		break
	else
		echo "Attempt $ATTEMPT failed: $OUTPUT"
		echo "Retrying in $RETRY_DELAY seconds..."
		sleep $RETRY_DELAY
		((ATTEMPT++))
	fi
done

if [[ $ATTEMPT -gt $MAX_RETRIES ]]; then
	echo "Failed to authorize ingress after $MAX_RETRIES attempts."
	exit 1
fi
	

# Create IAM role and instance profile
echo "Setting up IAM role and instance profile..."
aws iam create-role --role-name $INSTANCE_PROFILE_NAME \
  --assume-role-policy-document file://<(cat <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "ec2.amazonaws.com" },
    "Action": "sts:AssumeRole"
  }]
}
EOF
) || true


aws iam attach-role-policy --role-name $INSTANCE_PROFILE_NAME \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess || true

aws iam create-instance-profile --instance-profile-name $INSTANCE_PROFILE_NAME || true
aws iam add-role-to-instance-profile \
  --instance-profile-name $INSTANCE_PROFILE_NAME \
  --role-name $INSTANCE_PROFILE_NAME || true

echo "Waiting for IAM instance profile propagation..."
sleep 5

echo "Creating key pair..."

KEY_OUTPUT=$(aws ec2 create-key-pair \
	--key-name "$KEY_NAME" \
	--query 'KeyMaterial' \
	--output text \
	--region "$REGION" 2>&1)

if [[ $? -ne 0 ]]; then
	if [[ "$KEY_OUTPUT" == *"InvalidKeyPair.Duplicate" ]]; then
		echo "Key pair '$KEYNAME' already created."
		exit 1
	fi
else
	echo "$KEY_OUTPUT" > "$KEY_FILE"
	chmod 400 "$KEY_FILE"
	echo "Key pair created and saved to $KEY_FILE"
fi 

echo "Waiting for key propagation..."
sleep 5

USER_SCRIPT=$(cat <<EOF
#!/bin/bash
set -e
yum update -y
amazon-linux-extras install docker -y
service docker start
usermod -a -G docker ec2-user

yum install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -q awscliv2.zip
./aws/install

ACCOUNT_ID=\$(aws sts get-caller-identity --query "Account" --output text)
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin "\${ACCOUNT_ID}.dkr.ecr.$REGION.amazonaws.com"

aws ecr describe-repositories --repository-names "$ECR_REPO_NAME" --region "$REGION" >/dev/null 2>&1 || \
aws ecr create-repository --repository-name "$ECR_REPO_NAME" --region "$REGION"

docker pull "$DOCKER_IMAGE"
IMAGE_URI="\${ACCOUNT_ID}.dkr.ecr.$REGION.amazonaws.com/$ECR_REPO_NAME"
docker tag "$DOCKER_IMAGE" "\$IMAGE_URI"
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin "\${ACCOUNT_ID}.dkr.ecr.$REGION.amazonaws.com"
docker push "\$IMAGE_URI"

echo "Docker maybe finished...?"
EOF
)

# Launch EC2 instance
echo "Launching EC2 instance..."

INSTANCE_ID=$(aws ec2 run-instances \
  --image-id "$AMI_ID" \
  --count 1 \
  --instance-type "$INSTANCE_TYPE" \
  --key-name "$KEY_NAME" \
  --security-group-ids "$SECURITY_GROUP_ID" \
  --subnet-id "$RANDOM_SUBNET" \
  --block-device-mappings "[{\"DeviceName\":\"/dev/xvda\",\"Ebs\":{\"VolumeSize\":$VOLUME_SIZE}}]" \
  --iam-instance-profile Name=$INSTANCE_PROFILE_NAME \
  --associate-public-ip-address \
  --region "$REGION" \
  --user-data "$USER_SCRIPT" \
  --query 'Instances[0].InstanceId' --output text)

echo "EC2 Instance ID: $INSTANCE_ID"

## Wait for the instance to be running
aws ec2 wait instance-running --instance-ids "$INSTANCE_ID"
PUBLIC_IP=$(aws ec2 describe-instances --instance-ids "$INSTANCE_ID" \
  --query "Reservations[0].Instances[0].PublicIpAddress" --output text)

echo "If you wish to login a pem key has been put in your working directory. The instance public IP is: $PUBLIC_IP"
echo "It can take up to 15 minutes for an image to appear in your private repository."

#TODO shutdown ec2 after pushing
