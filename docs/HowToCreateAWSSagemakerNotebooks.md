# Using Amazon SageMaker AI

AWS offers different types of Notebook instances and now two SageMaker products. For these tutorials please use Amazon SageMaker AI. Within this offering, you will see  SageMaker Notebook Instances and SageMaker Studio. SageMaker Notebook Instances offer the most flexibility in terms of installing local software, while Studio allows for several IDEs and launching from custom containers. If you are following a tutorial that installs software or command line tools, follow the instructions for 1) SageMaker Notebook Instances.

### Set up a SageMaker Notebook Instance

1. In AWS console, type **Amazon SageMaker** in search bar and click it:

  ![selectsagemaker](/images/images_for_creating_AWS_notebooks/Screenshot1.png)

2. On the left side bar click **Notebooks**:

  ![Notebooks](/images/images_for_creating_AWS_notebooks/Screenshot2.png)

3. Click **Create notebook instance**:

  ![create_new_notebook](/images/images_for_creating_AWS_notebooks/Screenshot3.png)

4. Give a name to your notebook. Choose a notebook instance type based on needs, Amazon Linux 2 as platform identifier, volume. Optional, create idle-shut by selecting create new lifecycle configuration and copy and paste [idle-shutdown.sh](/idle-shutdown.sh) and create configuration. Then click Create notebook instance:

  ![environment](/images/images_for_creating_AWS_notebooks/Screenshot4.png)
   
5. It will take about 5 minutes, your notebook instance to get ready:

  ![pending](/images/images_for_creating_AWS_notebooks/Screenshot5.png)
   
   
6. **Open Jupyter Lab**:

  ![jupyterlab](/images/images_for_creating_AWS_notebooks/Screenshot6.png)

7. Clone an appropriate repository from GitHub.com:

  ![upload](/images/images_for_creating_AWS_notebooks/Screenshot7.png)

8. Select a notebook and then kernel:

  ![kernel](/images/images_for_creating_AWS_notebooks/Screenshot8.png)

9.  To clone in your git repositories you can either use the git UI built in or by using the terminal. Using the git UI select **Clone a Repository** then paste the repo url and click **Clone**. To clone via the terminal make sure that you are in the SageMaker directory then use the command git clone [repo url]. Once you have done this you should see the repo 

  ![Clone_UI](/images/images_for_creating_AWS_notebooks/Clone_UI.png)
  ![Clone_Terminal](/images/images_for_creating_AWS_notebooks/Clone_Terminal.png)

10. **IMPORTANT**: **Stop** the kernel at end of your work to avoid getting charged.

  ![resize image](/images/images_for_creating_AWS_notebooks/Screenshot9.png)



### Set up SageMaker Studio

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

