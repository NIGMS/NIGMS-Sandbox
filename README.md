# **National Institute of General Medical Sciences Cloud Learning Modules**


<!-- #region -->
# Introduction

This repository aims to teach students, researchers, and clinicians, among others, how to utilize the power of cloud technology for the benefit of life sciences applications and research. Here we present 12 cloud learning modules that represent a unique scientific workflow. Types of data used across the modules include but are not limited to genomics, methylomics, transcriptomics, proteomics, and medical imaging data across formats such as FASTA/FASTQ, SAM, BAM, CSV, PNG, and DICOM. Learning modules range in areas from introductory material to single-omics approaches, multi-omics techniques, single cell analyses, metagenomics, and AI/ML analyses of medical images.
![image1](images/Universities.png)


*The 12 topics and their authors are listed as follows:*

1. [Fundamentals of Bioinformatics](/Bioinformatics_for_Beginners_with_Terminal--Dartmouth_College/) -  Dartmouth College
2. [DNA Methylation Sequencing Analysis with WGBS](/Whole_Genome_Bisulfite_Sequencing--University_of_Hawaii_Manoa/) - University of Hawaii at Manoa
3. [Transcriptome Assembly Refinement and Applications](/RNA-Sequencing_Transcriptome_Assembly--MDI_Biological_Laboratory/) - MDI Biological Laboratory
4. [RNAseq Analysis](https://github.com/NIGMS/RNAseqUnivMaine) – University of Maine INBRE
5. [ATAC-Seq and Single Cell ATAC-Seq Analysis](/Interactive_Pipeline_for_differential_ATAC-Sequencing_Footprint_Analysis--University_of_Nebraska_Medical_Center/) - University of Nebraska
6. [Consensus Pathway Analysis in the Cloud](/Consensus_Pathway_Analysis_using_GCP--University_of_Nevada_Reno/) - University of Nevada Reno
7. [Proteomics Secondary Analysis](https://github.com/NIGMS/ProteomicsUAMS) – University of Arkansas for Medical Sciences
8. [Integrating Multi-Omics Datasets](/Transcriptomic_Epigenomic_Multi_Omics_Integration--University_of_North_Dakota/) - University of North Dakota
9. [Metagenomics Analysis of Biofilm-Microbiome](/Dockerized_Metagenomics_Analysis_of_Microbial_Communities_and_Biofilm--University_of_South_Dakota/) - University of South Dakota
10. [Data Science for Biology, An Introduction](/Intro_to_ML_Predicting_Covid_Cases--San_Francisco_State_University/) - San Francisco State University
11. [Biomarker Discovery with ML](/Analysis_of_Biomedical_Data_for_Biomarker_Discovery--University_of_Rhode_Island/) - University of Rhode Island
12. [Biomedical Imaging Analysis using AI/ML approaches](/Diving_into_Deep_Learning_for_Biomedical_Imaging_Data_Analysis--University_of_Arkansas_Fayetteville/) - University of Arkansas
<!-- #endregion -->

# Table of Contents
+ [Cloud Technology Utilized](#one)
+ [Cloud Module Prerequisites](#two)
+ [Resources](#three)
+ [Alternative Data Sources](#four)


## Cloud Technology Utilized <a name="one"></a>

The 12 NIGMS cloud modules utilize the following GCP services:  Cloud Storage, gcsfuse, VertexAI Workbench, Artifact Registry, Cloud Build, BigQuery, and Cloud Lifesciences API*. Technologies that support the cloud services mentioned include JupyterLab, Docker, Git, and life sciences software libraries such as [Bioconductor](https://www.bioconductor.org/) in R and the [Bioconda](https://bioconda.github.io/) Anaconda channel in Python.

<div style="font-size:75%;font-style: italic;">
*Google Batch is a newer service that offers similar functionality and may replace the Life Sciences API in the future. 
</div>

<!-- #region -->
## Cloud Module Prerequisites <a name="two"></a>

Each module has different infrastructure and software requirements. While many of the GCP services required overlap there are specifications that users should keep in mind before they start their self paced learning. More details can be found within each individual repository README. An overview is provided below: 

1. Fundamentals of Bioinformatics, Dartmouth College 
* default machine type: n1-standard-4
* Python 3 kernel
* env.yml contains necessary software requirements for easy installation

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Bioinformatics_for_Beginners_with_Terminal--Dartmouth_College/README.md"> Dartmouth README </A>
</div>

2. DNA Methylation Sequencing Analysis with WGBS, University of Hawaii at Manoa
* default machine type: n1-standard-4
* Python 3 kernel
* Nextflow Service Account

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Whole_Genome_Bisulfite_Sequencing--University_of_Hawaii_Manoa/README.md"> Hawaii README </A>
</div>

3. Transcriptome Assembly Refinement and Applications, MDI Biological Laboratory
* default machine type: n1-highmem-16
* Python 3 kernel
* Nextflow Service Account

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/RNA-Sequencing_Transcriptome_Assembly--MDI_Biological_Laboratory/README.md"> MDI README </A>
</div>

4. ATAC-Seq and Single Cell ATAC-Seq Analysis, University of Nebraska
Modules 1-3: 
* default machine type: n1-standard-4
* Python 3 kernel
Module 4:
* T4 GPU attached
* RAPIDS VertexAI image

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Interactive_Pipeline_for_differential_ATAC-Sequencing_Footprint_Analysis--University_of_Nebraska_Medical_Center/README.md"> Nebraska README </A>
</div>

5. Consensus Pathway Analysis in the Cloud, University of Nevada Reno
* default machinetype: n1-standard-4
* R 4.1 kernel

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Consensus_Pathway_Analysis_using_GCP--University_of_Nevada_Reno/README.md"> Nevada README </A>
</div>

6. Integrating Multi-Omics Datasets, University of North Dakota
* default machinetype: n1-standard-4
* R 4.1 kernel
* conda_environment.yml contains necessary software(s)
* Nextflow Service Account


<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/RNA-Sequencing_Transcriptome_Assembly--MDI_Biological_Laboratory
Transcriptomic_Epigenomic_Multi_Omics_Integration--University_of_North_Dakota/README.md"> North Dakota README </A>
</div>

7. Metagenomics Analysis of Biofilm-Microbiome, University of South Dakota
* default machinetype: n1-standard-8
* Python 3 kernel
* custom service account
* custom image
* requirements.yaml

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Dockerized_Metagenomics_Analysis_of_Microbial_Communities_and_Biofilm--University_of_South_Dakota/README.md"> South Dakota README </A>
</div>

8. Data Science for Biology, An Introduction, San Francisco State University
* default machine type: n1-standard-4
* Python 3 kernel

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Intro_to_ML_Predicting_Covid_Cases--San_Francisco_State_University/README.md"> San Francisco README </A>
</div>

9. Biomarker Discovery with ML, University of Rhode Island
* default machine type: n1-standard-4
* R 4.1 kernel

<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Analysis_of_Biomedical_Data_for_Biomarker_Discovery--University_of_Rhode_Island/README.md"> Rhode Island README </A>
</div>

10. Biomedical Imaging Analysis using AI/ML approaches, University of Arkansas
* default machine type: n1-standard-4
* Python 3 kernel


<div style="font-size:90%;font-style: italic;text-indent: 20px">
Detailed software requirements: <A href="/Diving_into_Deep_Learning_for_Biomedical_Imaging_Data_Analysis--University_of_Arkansas_Fayetteville/README.md"> Arkansas README </A>
</div>
<br>
<br>

❗ **The following documentation provided in this repository shows users how to accomplish each prerequisite listed above.** ❗ 


| NIGMS "How to" Document                                                                       | Link                                                                                     |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| How to create conda virtual environments to use as jupyter kernels                            | [How to use conda environments as kernels](/docs/How_to_use_conda_envs_as_kernels.ipynb) |                 
| How to mount cloud storage buckets in your vertex ai notebook with gcsfuse                    | [How to mount cloud storage buckets](/docs/How_to_mount_buckets.ipynb)                   |
| How to create custom images for VertexAI                                                      | [How to create custom VertexAI images](/docs/How_to_create_custom_VertexAI_images.ipynb) |

<!-- #endregion -->

<!-- #region -->
## Resources <a name="three"></a>
In the below section we define the GCP services utilized across the learning modules. You can find an additional curated list of GCP tutorials in this repository under docs: [GCP Resources detailed](./docs/GoogleCloudPlatformResources.md)

### Google Cloud Platform resources

1. **IAM - https://cloud.google.com/iam/docs/overview** \
IAM in GCP allows you to manage access control by defining who (identity) has what access (role) for which resource. In IAM, permission to access a resource isn't granted directly to the end user. Instead, permissions are grouped into roles, and roles are granted to authenticated principals. 


2. **Billing - https://cloud.google.com/billing/docs** \
To use Google Cloud services, you must have a valid Cloud Billing account, and must link it to your Google Cloud projects. Your project's Google Cloud usage is charged to the linked Cloud Billing account. When you sign up for [NIH Cloud Lab](https://cloud.nih.gov/resources/cloudlab/) you will access an account loaded with credits for you to experiment with.


3. **Cloud Storage - https://cloud.google.com/storage/docs/introduction** \
Cloud Storage is a service for storing your objects in Google Cloud. An object is an immutable piece of data consisting of a file of any format. You store objects in containers called buckets. All buckets are associated with a project, and you can group your projects under an organization. 


4. **VertexAI - https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform** \
Vertex AI brings AutoML and AI Platform together into a unified API, client library, and user interface. AutoML lets you train models on image, tabular, text, and video datasets without writing code, while training in AI Platform lets you run custom training code. With Vertex AI, both AutoML training and custom training are available options. Whichever option you choose for training, you can save models, deploy models, and request predictions with Vertex AI. VertexAI implements JupyterLab in VertexAI Workbench. 


 
5. **Cloud Build - https://cloud.google.com/build/docs** \
Cloud Build is a service that executes your builds on Google Cloud infrastructure. Cloud Build can import source code from Cloud Storage, Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your specifications, and produce artifacts such as Docker containers or Java archives.


6. **Cloud Life Sciences API - https://cloud.google.com/life-sciences/docs/process-genomic-data** \
Cloud Life Sciences is a suite of services and tools for managing, processing, and transforming life sciences data. Cloud Life Sciences (formerly Google Genomics) enables the life sciences community to process biomedical data at scale. Cost effective and supported by a growing partner ecosystem, Cloud Life Sciences lets you focus on analyzing data and reproducing results.


7. **Operations (formerly Stackdriver) https://cloud.google.com/stackdriver/docs** \
Operations, formerly known as Stackdriver, is composed of Monitoring and Logging. Cloud Monitoring collects metrics, events, and metadata from Google Cloud, Amazon Web Services (AWS), hosted uptime probes, and application instrumentation. Using the BindPlane service, you can also collect this data from over 150 common application components, on-premise systems, and hybrid cloud systems. Google Cloud's operations suite ingests that data and generates insights via dashboards, charts, and alerts. BindPlane is included with your Google Cloud project at no additional cost.

Cloud Logging is a fully managed service that allows you to store, search, analyze, monitor, and alert on logging data and events from Google Cloud and Amazon Web Services. You can collect logging data from over 150 common application components, on-premises systems, and hybrid cloud systems.



<!-- #endregion -->

### NIH Cloud Lab

NIH Cloud Lab’s goal is to make the cloud very easy and accessible for you, so that you can spend less time on administrative tasks and focus on your research. NIH Cloud Lab hosts cloud service provider-specific repositories with tutorials, guides, and useful resources. NIH Cloud Lab's GCP repository (https://github.com/STRIDES/NIHCloudLabGCP) can be used to learn how to use GCP by exploring the linked resources and completing the tutorials.

[NIH Cloud Lab Tutorials](https://github.com/STRIDES/NIHCloudLabGCP/tree/main/tutorials) include the following topics:
+ Biomedical Workflows on GCP
+ Download SRA Data
+ Variant Calling
+ VCF Query
+ GWAS
+ Proteomics
+ Medical Imaging
+ RNAseq
+ scRNAseq
+ BLAST
+ Long Read Sequencing Analysis
+ Public Data Sets
+ Using the Life Sciences API




## Alternative Data Sources <a name="four"></a>

Where can users get similar data to run through these tutorials with their own datasets or alternative datasets of interest? 

1. SRA \
Sequence Read Archive (SRA) data, available through multiple cloud providers and NCBI servers, is the largest publicly available repository of high throughput sequencing data. The archive accepts data from all branches of life as well as metagenomic and environmental surveys. SRA stores raw sequencing data and alignment information to enhance reproducibility and facilitate new discoveries through data analysis. Learn more here: https://www.ncbi.nlm.nih.gov/sra

2. GEO \
GEO is a public functional genomics data repository supporting MIAME-compliant data submissions. Array- and sequence-based data are accepted. Tools are provided to help users query and download experiments and curated gene expression profiles. Learn more here: https://www.ncbi.nlm.nih.gov/geo/ 

3. MEDMNIST \
The MedMNIST v2 dataset consists of 12 pre-processed 2D datasets and 6 pre-processed 3D datasets from selected sources covering primary data modalities (e.g., X-Ray, OCT, Ultrasound, CT, Electron Microscope), diverse classification tasks (binary/multi-class, ordinal regression and multi-label) and data scales (from 100 to 100,000). For simplicity, we call the collection of all 2D datasets as MedMNIST2D, and that of 3D as MedMNIST3D. MedMNIST can be downloaded through pip. Learn more here: https://medmnist.com/

4. Google Public Dataset Program - https://services.google.com/fh/files/misc/public_datasets_one_pager.pdf \
Google Cloud Public Datasets facilitate access to high-demand public datasets making it easy for you to access and uncover new insights in the cloud. By hosting these datasets in BigQuery and Google Cloud Storage, you can seamlessly experience the full value of Google Cloud with the touch of a button. Explore public datasets stored in buckets here: https://cloud.google.com/storage/docs/access-public-data.
Explore public datasets stored in BigQuery here: https://cloud.google.com/bigquery/public-data


```python

```
