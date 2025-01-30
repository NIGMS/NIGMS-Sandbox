# Pushing Public Docker Images to Private ECR

We will go through how to push a public docker image to a private repository in Elastic Container Registry.

## Part 1: Pull a Docker image

* In AWS console, In a notebook instance, Open JupyterLab:

  ![](../images/ECR/5.PNG)

* Open Terminal:

  ![](../images/ECR/6.PNG)

* Pull a Docker iamge: `docker pull public.ecr.aws/v8e3m3v4/sagemaker-studio/r:latest`

  ![](../images/ECR/7.PNG)

## Part 2: Create a repository in ECR

* In AWS console, type *ECR* in search bar and then click **Elastic Container Registry**:

  ![](../images/ECR/1.PNG)

* Click **Create repository**:

  ![](../images/ECR/2.PNG)

* Give a name and then create the repository:

  ![](../images/ECR/3.PNG)

* Copy URI of your repository for the next part:

  ![](../images/ECR/4.PNG)

## Part 3: Push Docker image to ECR

* Retrieve an authentication token and authenticate your Docker client to your registry:

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 664418964547.dkr.ecr.us-east-1.amazonaws.com/sagemaker/r-kernel`

![](../images/ECR/8.PNG)

* Tag your image so you can push the image to this repository:

`docker tag public.ecr.aws/v8e3m3v4/sagemaker-studio/r:latest 664418964547.dkr.ecr.us-east-1.amazonaws.com/sagemaker/r-kernel:latest`

![](../images/ECR/9.PNG)

* Run the following command to push this image to your newly created AWS repository:

`docker push 664418964547.dkr.ecr.us-east-1.amazonaws.com/sagemaker/r-kernel:latest`

![](../images/ECR/10.PNG)