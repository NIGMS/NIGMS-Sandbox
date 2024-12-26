# Set Up a JupyterLab with a Custom Docker Image

1. In Amazon SageMaker AI, **Create domain**:

![](/images/images_custom_kernel/Capture1.PNG)

2. Leave the **Quick setup** and click **Set up**:

![](/images/images-custom-kernel/Capture2.PNG)

3. After having your domain ready, go to **Environment** tab and click **Attach image**:

![](/images/images-custom-kernel/Capture3.PNG)

4. Under **New image**, enter and ECR image URL, click **Next**:

![](/images/images-custom-kernel/Capture4.PNG)

5. Give a name to your image, select **JupyterLab image**, and **Submit**:

![](/images/images-custom-kernel/Capture5.PNG)

6. In **Studio** tab, **Select Domain** and then **Open Studio**:

![](/images/images-custom-kernel/Capture6.PNG)

7. Select **Jupyterlab**, and then click **Create JupyterLab Space**:

![](/images/images-custom-kernel/Capture7.PNG)

8. Give a name, and then **Create space**:

![](/images/images-custom-kernel/Capture8.PNG)

9. Select the custom image, instance type, and then **Run space**:

![](/images/images-custom-kernel/Capture9.PNG)

10. **Open JupyterLab**:

![](/images/images-custom-kernel/Capture10.PNG)