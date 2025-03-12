## How to Launch AWS Batch for Nextflow Workflows

If you would like to skip building in the cloud and just launch the stack please click the button below and follow the instructions to complete stack deployment. The deployment should take ~5 min and then the resources will be ready for use.

[![Launch Stack](/images/images_for_creating_AWSBatch/LaunchStack.jpg)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=aws-batch-nigms&templateURL=https://nigms-sandbox.s3.us-east-1.amazonaws.com/cf-templates/AWSBatch_template.yaml ){:target="_blank"}

Select `Next` at the bottom right. ![Launch Stack Select](/images/images_for_creating_AWSBatch/LaunchStack_select.png)

Select `Next` again at the bottom right of the screen. ![Launch Stack Specify](/images/images_for_creating_AWSBatch/LaunchStack_specify.png)

Select `I acknowledge` that AWS CloudFormation might create IAM resources and Next. ![Launch Stack Configure](/images/images_for_creating_AWSBatch/LaunchStack_configure.png)

Review and select `Submit`. ![Launch Stack Review](/images/images_for_creating_AWSBatch/LaunchStack_review.png)

When creating the SageMaker notebook please select the corresponding IAM role. The role name will start with aws-batch-nigms-SageMakerExecutionrole-*unique_identifier*. ![SageMaker IAM Role](/images/images_for_creating_AWSBatch/SageMaker_IAM_Role.png)
