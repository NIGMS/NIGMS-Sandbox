## How to Reuse AWS Batch Resources for Nextflow Workflows
If you have already launched the AWS Batch Stack using the cloud formation template from [HowToLaunchAWSBatch.md](/docs/HowToLaunchAWSBatch.md) or created your own AWS batch environment using [AWS-Batch-Setup.md](/docs/AWS-Batch-Setup.md) then you can reuse the resources created without having to re-launch the stack. Please follow the instructions below for how to re-use the resources when AWS Batch environment has already been created. 

### Re-use IAM role in SageMaker Notebook Instance 
1. In the AWS console, when creating or editing a notebook instance, under **Permissions and encryption** select the drop down list under **IAM role**. If you are in the same region as where your AWS Batch environment was made, you should be able to access the IAM role created for use with AWS Batch. 

![ClickDropdown](/images/images_for_resuing_AWSBatch_Resources/SageMakerNotebook_Permissions.png)

2. Select the correct IAM role. If the launch stack template was used, the corresponding IAM role name should be `aws-batch-nigms-SageMakerExecutionRole`

![SelectIAMrole](/images/images_for_resuing_AWSBatch_Resources/SageMakerNotebook_IAMrole.png)
