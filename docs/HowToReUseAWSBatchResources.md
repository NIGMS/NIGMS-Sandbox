## How to Reuse AWS Batch Resources for Nextflow Workflows
If you have already launched the AWS Batch Stack using the cloud formation template from [HowToLaunchAWSBatch.md](/docs/HowToLaunchAWSBatch.md) or created your own AWS batch environment using [AWS-Batch-Setup.md](/docs/AWS-Batch-Setup.md) then you can reuse the resources created without having to re-launch the stack. Please follow the instructions below for how to re-use the resources when AWS Batch environment has already been created. 

### Re-use IAM role in SageMaker Notebook Instance 
1. In the AWS console, when creating or editing a notebook instance, under **Permissions and encryption** select the drop down list under **IAM role**. If you are in the same region as where your AWS Batch environment was made, you should be able to access the IAM role created for use with AWS Batch. 

![ClickDropdown](/images/images_for_resuing_AWSBatch_Resources/SageMakerNotebook_Permissions.png)

2. Select the correct IAM role. If the launch stack template was used, the corresponding IAM role name should be `aws-batch-nigms-SageMakerExecutionRole`. 

![SelectIAMrole](/images/images_for_resuing_AWSBatch_Resources/SageMakerNotebook_IAMrole.png)

### Re-launching AWS Batch Stack template 
AWS Batch is a fully managed service that enables developers, scientists, and engineers to easily and efficently run hundreds of thousands of batch computing jobs. It dynamically provisions the optimal quantity and type of compute resources based on the volume and specific resource requirements of the submitted batch jobs. This allows users to focus on analyzing results and solving problems rather than managing infrastructure. This is why we have created the option to deploy the AWS Batch Stack through a template and the reason that the stack does not have to be launched multiple times. If you must re-launch the stack from [HowToLaunchAWSBatch.md](/docs/HowToLaunchAWSBatch.md), then please follow the proceeding steps: 

1. Search **lambda** in the AWS console and select Lambda: 
![AWSConsoleLambda](/images/images_for_resuing_AWSBatch_Resources/AWSConsoleLambda.png)

2. Select the **GetNetworkingFunction** and click **Actions** on the top-right hand corner next to Create function. Select **Delete**.
![SelectFunctionDelete](/images/images_for_resuing_AWSBatch_Resources/SelectFunctionDelete.png)

3. Type **confirm** and click **Delete**. 
![ConfirmDelete](/images/images_for_resuing_AWSBatch_Resources/ConfirmDelete.png)

4. Search **cloud formation** in the AWS console and select CloudFormation: 
![AWSConsoleCloudFormation](/images/images_for_resuing_AWSBatch_Resources/CloudFormation.png)

5. Click on the hyperlink name of the stack to see Stack details: 
![StackHyperlink](/images/images_for_resuing_AWSBatch_Resources/StackHyperlink.png) 

6. Select **Resources** and select the batch bucket resource. The delete will fail if there is data within the bucket so move or delete data within batch bucket. 
![ResourcesBatchBucket](/images/images_for_resuing_AWSBatch_Resources/ResourcesBatchBucket.png)

7. Ensure the correct stack is selected and click Delete.
![StackSelectDelete](/images/images_for_resuing_AWSBatch_Resources/DeleteStack.png)

6. Select Delete. The stack should now be deleted. 
![StackDelete](/images/images_for_resuing_AWSBatch_Resources/StackDelete.png)

You can now re-launch the AWS Stack from the cloud formation template link. 