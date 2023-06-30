# Using VertexAI Notebooks

### Spin up a VertexAI Virtual Machine
1. Start by clicking the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. 

<img src="/images/1_select_vertexAI.png" width="550" height="350">

2. Click `New Notebook` and select `R 4.1` for the kernel, although note that you can use a variety of environments including Python, R, PyTorch, TensorFlow, and others. This can also be changed later. 

<img src="/images/2_select_kernel_R.png" width="550" height="600">

3. Name your notebook a globally unique name. Note that in GCP you can only use dash, not underscore. For region select the region closest to where you live, or else the region where your cloud storage bucket is located. Now click the pencil icon next to `Notebook properties`.

<img src="/images/3_name_notebook.png" width="550" height="500">

4. When the new window opens, you can modify the rest of the settings. For operating system select 'Debian 10', for 'Environment' select your desired Environment. This where you can change this if you selected something different before. Under `Machine configuration > Machine type` select your machine type. For this tutorial you can get away with using `e2-standard-4`, but you will likely want a more powerful machine for other workflows. Read more about machine families on GCP [here](https://cloud.google.com/compute/docs/machine-types), about the specifics of general purpose machine types within machine families [here](https://cloud.google.com/compute/docs/general-purpose-machines). You can follow the links in those doc pages for Compute, Memory, or Accelerator optimized machine types as well. You can figure out the cost of your selected machine [here](https://cloud.google.com/compute/all-pricing). _Remember that as long as your notebook is running (and not stopped) you will be charged per second of use. This is especially important to remember for GPU machines as these will consume your budget quickly. Consider installing an [auto-shutdown script](/docs/compute-engine-idle-shutdown.md) to prevent this._ Leave all other settings as default and click **Create**.

<img src="/images/4_select_environment.png" width="550" height="400">

5. It will take a minute or two for your new notebook environment to spin up so go brew some coffee and come back. Once the status changes from a blue spinning ball to `Open JUPYTERLAB` then your VM is ready. You may need to click `Refresh` at the top of the page to see the status change. That is a good rule of thumb on GCP; if you are waiting on something to spin up, try clicking refresh and it may already be done. 

<img src="/images/5_launch_notebooks.png" width="550" height="150">


### (Bonus) Using the new Managed Notebooks feature
At the time of writing, Google had just rolled out a new feature in Vertex AI called `Managed Notebooks`, which now differ from the `User Managed Notebooks`. You can use either one for this tutorial, but the nice thing about the new `Managed Notebooks` is that you can schedule them, or just execute them similar to submitting a job to a slurm cluster. Read the documentation for [scheduling a notebook](https://cloud.google.com/vertex-ai/docs/workbench/managed/schedule-managed-notebooks-run-quickstart). Note that scheduled notebooks will be run on remote compute resources, so you need to treat them like a fresh install, copy your data in, install all packages, etc. Don't expect that because you have data/dependencies copied to your current environment they will be present when your scheduled notebook is run. Also, when you spin up the Managed Notebook, make sure you select `Single User` rather than Service Account to avoid permission conflicts. You can also resize the machine on the fly (without shutting down), and there are some extra compute environments available. However, we have observed that conda is tightly controlled on these machines, so if you decide to try them and have issues with conda, switch back to the User Managed Notebooks.

### Import custom notebook and data

1. Now click the git icon on the middle left bar (it kind of looks like the letter 'T' with a tilt). Click `Clone a Repository`, and then paste `https://github.com/STRIDES/NIHCloudLabGCP.git` into the box. You can also open a terminal and paste in the following:

```
git clone https://github.com/STRIDES/NIHCloudLabGCP.git
```

<img src="/images/1_clone_repo_gcp.png" width="550" height="400">

2. Now you have the NIHCloudLabGCP directory available. Navigate to NIHCloudLabGCP > tutorials > notebooks > GWASCoatColor > GWAS_coat_color.ipynb.
Explore this notebook and see how data moves into and out of the Vertex AI environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu. You can easily switch between different kernels in the top right. If you had selected Python3 when starting the instance, you would only have access to Python, but would need a different instance to open or create an R notebook for example. However, if you start with R, then can switch between R and Python. After finishing this notebook, move onto the SRA_and_BigQuery notebook to learn about some key GCP skills, 
like importing (SRA) data, making a cloud storage bucket and moving data in and out of the bucket, and finally how to query VCF files with BigQuery.

<img src="/images/2_GWAS_notebook.png" width="550" height="350">

Here are a few tips if you are new to notebooks: The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

Another thing worth noting is that when you run a cell, sometimes it doesn't produce any output; however, processes are running in the background. If the brackets next to a cell have an * then it is still running. You can also look at the bottom where the kernel is listed (e.g., Python 3 | status) and it will show either Idle or Busy depending on whether anything is running or not. 

<img src="/images/3_busy_cell.png" width="550" height="550">

