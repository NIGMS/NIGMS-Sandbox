# Using VertexAI Notebooks

### 1. Spin up an Instance
1. Start by clicking the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. 

![screenshot showing how to select Vertex AI workbench](/images/1_select_vertexAI.png)

2. If not already selected, click **Instances**, then **Instances**
3. Click **+ Create New**

![image showing how to select instance](/images/images_for_creating_GCP_instances/2_select_workbench_instance.png)

4. Select **Advanced Options** at the bottom of the **New Instance** pop-up window
5. Provide a name for your new instance using letters, numbers, and hyphens (-). Select a region and zone for the new instance. For best network performance, select the region that is geographically closest to you.  Click **Continue**

![image showing to select advanced options](/images/images_for_creating_GCP_instances/3_select_advanced_options.png)

6. On the Environment screen, select "Use the latest version" if not already selected. Skip the other sections. Click **Continue**.

![image showing to select environment](/images/images_for_creating_GCP_instances/4_instance_environment.png) 

7. On the Machine type screen, select the desired number of CPUs/GPUs. This is usually specified by the tutorial you are completing.

![image showing machine type selection](/images/images_for_creating_GCP_instances/5_instance_machine_type.png)

8. On the same screen, verify that **Enable Idle Shutdown** is selected and specify the idle minutes for shutdown. This means it will shutdown automatically after this many minutes. We recommend 30 minutes. Click **Create**.  It will take a few minutes for your instance to spin up.

![image showing idle shutdown selection](/images/images_for_creating_GCP_instances/6_instance_idle_shutdown.png) 

9. The remaining sections can be left as default for our purposes.  Further details can be found in the official documentation: [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs/workbench/instances/create)

### 2. Spin up a User-Managed Notebook Instance
1. Start by clicking the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. 

![screenshot showing how to select Vertex AI workbench](/images/1_select_vertexAI.png)

2. Click `New Notebook` and select your desired kernel. You can use a variety of environments including Python, R, PyTorch, TensorFlow, and others. This can also be changed later. Check out the [required environments](https://github.com/NIGMS/NIGMS-Sandbox/tree/main#cloud-module-prerequisites) for your module of interest to confirm which kernel you should choose.

![screenshot showing how to select an R kernel from Vertex AI workbench](/images/2_select_kernel_R.png)

3. Name your notebook a globally unique name. Note that in GCP you can only use dash, not underscore. For region select the region closest to where you live, or else the region where your cloud storage bucket is located. Now click the pencil icon next to `Notebook properties`.

![screenshot showing how to name a notebook](/images/3_name_notebook.png)

4. When the new window opens, you can modify the rest of the settings. For operating system select 'Debian 10', for 'Environment' select your desired Environment. This where you can change this if you selected something different before. Under `Machine configuration > Machine type` select your machine type. For this tutorial you can get away with using `e2-standard-4`, but you will likely want a more powerful machine for other workflows. Read more about machine families on GCP [here](https://cloud.google.com/compute/docs/machine-types), about the specifics of general purpose machine types within machine families [here](https://cloud.google.com/compute/docs/general-purpose-machines). You can follow the links in those doc pages for Compute, Memory, or Accelerator optimized machine types as well. You can figure out the cost of your selected machine [here](https://cloud.google.com/compute/all-pricing). _Remember that as long as your notebook is running (and not stopped) you will be charged per second of use. This is especially important to remember for GPU machines as these will consume your budget quickly. Consider installing an [auto-shutdown script](/docs/compute-engine-idle-shutdown.md) to prevent this._ Leave all other settings as default and click **Create**.

![screenshot showing how to setup the environment when creating a virtual machine](/images/4_select_environment.png)

5. It will take a minute or two for your new notebook environment to spin up so go brew some coffee and come back. Once the status changes from a blue spinning ball to `OPEN JUPYTERLAB` then your VM is ready. You may need to click `Refresh` at the top of the page to see the status change. That is a good rule of thumb on GCP; if you are waiting on something to spin up, try clicking refresh and it may already be done. 

![screenshot showing how to start the notebook by clicking OPEN JUPYTERLAB](/images/5_launch_notebooks.png)


### 3. Import custom notebook and data

1. Now click the git icon on the middle left bar (it kind of looks like the letter 'T' with a tilt). Click `Clone a Repository`, and then paste `https://github.com/NIGMS/NIGMS-Sandbox.git` into the box. From here you can explore the different modules that are available and clone them into your notebook. You can also clone this repository by opening a terminal and pasting in the following:

```
git clone https://github.com/NIGMS/NIGMS-Sandbox.git
```

![screenshot showing how to clone a github repository by using the git button](/images/1_clone_repo_gcp.png)

2. After you clone a training module, you can explore the notebooks and see how data moves into and out of the Vertex AI environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu. You can easily switch between different kernels in the top right. If you had selected Python3 when starting the instance, you would only have access to Python, but would need a different instance to open or create an R notebook for example. However, if you start with R, then you can switch between R and Python.

Here are a few tips if you are new to notebooks: The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

Another thing worth noting is that when you run a cell, sometimes it doesn't produce any output; however, processes are running in the background. If the brackets next to a cell have an * then it is still running. You can also look at the bottom where the kernel is listed (e.g., Python 3 | status) and it will show either Idle or Busy depending on whether anything is running or not. 

![screenshot showing an asterisk in the cell indicating that the cell is running](/images/3_busy_cell.png)

