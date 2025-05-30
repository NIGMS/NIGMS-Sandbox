# Using Amazon SageMaker AI

AWS offers different types of Notebook instances and now two SageMaker products. For these tutorials please use Amazon SageMaker AI. Within this offering, you will see  SageMaker Notebook Instances and SageMaker Studio. SageMaker Notebook Instances offer the most flexibility in terms of installing local software, while Studio allows for several IDEs and launching from custom containers. Studio is primarily designed for building and deploying AI models, but in our case, it allows us to launch from custom containers that allow you to run modules without installing any software. As such, if you are using a module that installs software or command line tools, follow the instructions for [1) SageMaker AI Notebook Instances](#Using-SageMaker-Notebook-Instances) and pay attention to the README for each module to select the correct machine type and EBS storage. If you are running a module that launches from a container, then follow [2) SageMaker AI Studio Instances](#Using-SageMaker-Studio), and likewise, follow the instructions of your module's README on specifications.

:exclamation: Please note that your interface may look different from the screenshots as the AWS interface continues to evolve.

### Using SageMaker Notebook Instances

:sparkles: If you prefer to follow the AWS documentation directly, go to [this page](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html)

1. In AWS console, type **Amazon SageMaker AI** in search bar and click it:

  ![selectsagemaker](/images/images_for_creating_AWS_notebooks/1-sagemakerAI.png)

2. On the left side bar click **Notebooks**:

  ![Notebooks](/images/images_for_creating_AWS_notebooks/Screenshot2.png)

3. Click **Create notebook instance**:

  ![create_new_notebook](/images/images_for_creating_AWS_notebooks/Screenshot3.png)

4. (1) Give a unique name to your notebook. (2) Choose a notebook instance type based on the specifications of your module's README. You can view all available machine types [here](https://aws.amazon.com/ec2/instance-types/). (3) For Platform, the default is fine unless otherwise specified in your module. (4) Click the dropdown for *Additional Configuration*. We will do two things here: (5) For Volume size in GB, make sure to follow the instructions of your module, otherwise, give the instance 200 GB. (6) Create your Lifecycle configuration (see step 5 below) and then select it here.

  ![environment](/images/images_for_creating_AWS_notebooks/2-sagemaker-instance.png)

5. Idle Shutdown allows your VM to shut off even if you forget to stop it. Click the dropdown and select *Create a new lifecycle configuration*. In the pop up box, paste in [this script](/idle-shutdown.sh) and then click *Create configuration*. You can leave all other steps as default.

  ![idle-shutdown](/images/images_for_creating_AWS_notebooks/3-idle-shutdown.png)

6. Now click **Create notebook instance**.

  ![create-notebook-instance](/images/images_for_creating_AWS_notebooks/4-click-create.png)
   
7. Wait about 5 minutes until your notebook says `InService`, then click **Open JupyterLab**.
   
  ![jupyterlab](/images/images_for_creating_AWS_notebooks/Screenshot6.png)

9. Clone your module of interest from GitHub either using the instructions in this screenshot or [like this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

  ![upload](/images/images_for_creating_AWS_notebooks/Screenshot7.png)

8. Select a notebook and then kernel:

  ![kernel](/images/images_for_creating_AWS_notebooks/Screenshot8.png)

10. **IMPORTANT**: **Stop** the kernel at end of your work to avoid getting charged. When you are finished with a module, delete the instance to prevent all future charges.

  ![resize image](/images/images_for_creating_AWS_notebooks/Screenshot9.png)



### Using SageMaker Studio

1. In AWS console, type **Amazon SageMaker** in search bar and click it:

  ![selectsagemaker](/images/images_for_creating_AWS_notebooks/Screenshot1.png)

2. On the left side bar click **Domains**:

  ![Domains](/images/images_for_creating_AWS_notebooks/Screenshot10.png)

3. Click **Create domain**:

  ![Create_domain](/images/images_for_creating_AWS_notebooks/Screenshot11.png)

4. Select **Set up for single user (Quick setup)** and then click **Set up**:

  ![Domain Setup](/images/images_for_creating_AWS_notebooks/Screenshot12.png)
   
5. It will take a few minutes for the domain to setup:

  ![pending](/images/images_for_creating_AWS_notebooks/Screenshot13.png)
   
6. Once the SageMaker Domain is setup, click **Studio** on the left sidebar:

  ![Studio](/images/images_for_creating_AWS_notebooks/Screenshot14.png)

7. Make sure that **Select Domain** and **Select user profile** contain domain and user then click **Open Studio**:

  ![Launch Studio](/images/images_for_creating_AWS_notebooks/Screenshot15.png)

8. This should take you to SageMaker Studio home:

  ![SageMaker Studio Home](/images/images_for_creating_AWS_notebooks/Screenshot16.png)


  ### Option 1 - JupyterLab 

1. Once in studio select **JupyterLab** on the top left under **Applications**:

  ![Launch JupyterLab](/images/images_for_creating_AWS_notebooks/Screenshot17.png)

2. Select **Create JupyterLab Space**:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot18.png)

3. Assign a name to the space,choose either to share domain or create private space, then select **Create Space**:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot19.png)

4. Choose **Instance** and **Storage(GB)** based upon expected usage then select **Run space**: 

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot20.png)

5. Wait for the space to start up and then select Open JupyterLab once ready:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot21.png)
  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot22.png)

6. After you are done working go back to JupyterLab and shutoff your instance by clicking Stop:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot23.png)

7. Wait until the status shows stopped for all unused instances:

  ![Launch JupyterLab](/images/images_for_creating_AWS_notebooks/Screenshot24.png)



### Option 2 - Code Editor

1. Once in studio select **Code Editor** on the top left under **Applications**:

  ![Launch JupyterLab](/images/images_for_creating_AWS_notebooks/Screenshot25.png)

2. Select **Create Code Editor Space**:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot26.png)

3. Assign a name to the space and select **Create Space**:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot27.png)

4. Choose **Instance** and **Storage(GB)** based upon expected usage then select **Run space**: 

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot28.png)

5. Wait for the space to start up and then select ***Open Code Editor*** once ready:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot29.png)
  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot30.png)

6. Once in code editor clone in your repository. This can be done by selecting the git icon, select **Clone Repository**, copy the web url into the box and then select **Clone from URL**. Alternatively you can open a terminal then use the command git clone web url. Once you do this cd into the cloned repository. If it doesn't show up in your folders select the file icon open folder and select the repository you cloned in. 

  ![Clone For Code Editor](/images/images_for_creating_AWS_notebooks/Clone_CodeEditor.png)

7. After working go back to Code Editor and stop the now unused instance by clicking ***Stop***:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot31.png)

8. Wait for the Status to show as Stopped:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot32.png)


### Managing Running Instances
 To check the active resources the Running Instances section was added. Below explains where it is and how to check what is actively running. 

 1. Go to **Running insances** within SageMaker Studio and make sure all instances being unused are stopped. If there are unused instances in the Running status select the associated stop action:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot33.png)

2. Wait for the instances to stop:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot34.png)

### Deleting Instances
1. Go to the Domain you are seeking to delete a instance. :

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot35.png)

2. After go to **Running insances** within SageMaker Studio and make sure all instances being unused are stopped:

  ![JupyterLab Space](/images/images_for_creating_AWS_notebooks/Screenshot36.png)

