# **National Institute of General Medical Sciences Cloud Learning Modules**


# Introduction

This repository aims to teach students, researchers, and clinicians, among others, how to utilize the power of cloud technology for the benefit of life sciences applications and research. Here we present 26 cloud learning modules that represent a unique use case or scientific workflow. Types of data used across the modules include but are not limited to genomics, methylomics, transcriptomics, proteomics, and medical imaging data across formats such as FASTA/FASTQ, SAM, BAM, CSV, PNG, and DICOM. Learning modules range in areas from introductory material to single-omics approaches, multi-omics techniques, single cell analysis, metagenomics, and AI/ML imaging applications. 

These modules run in Amazon Web Services, Microsoft Azure, and Google Cloud. All modules will be available across the three cloud platforms in 2027, but you may notice that a given module is only available in one or two of these platforms at this time. You can run these modules in any cloud account, but we encourage users to request access to an [NIH Cloud Lab](https://cloud.nih.gov/resources/cloudlab/) account for an optimal experience. 

To get started with any of the cloud platforms, visit the NIH Cloud Lab Jumpstart Pages for [AWS](https://cloud.nih.gov/resources/cloudlab/aws-jumpstart/), [Azure](https://cloud.nih.gov/resources/cloudlab/azure-jumpstart/), or [Google Cloud](https://cloud.nih.gov/resources/cloudlab/google-cloud-jumpstart/), or visit the tutorial pages: [AWS](https://github.com/STRIDES/NIHCloudLabAWS), [Azure](https://github.com/STRIDES/NIHCloudLabAzure), [GCP](https://github.com/STRIDES/NIHCloudLabGCP). 

:exclamation: _If you require support at any time, please [open an issue on GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) for the module in question, or [send us an informative email](https://stackoverflow.com/help/how-to-ask) at CloudLab@nih.gov._


![image1](images/Universities.png)

# Table of Contents
+ [Available Modules](#modules)
+ [Recomended Learning Pathways](#pathways)

# Available Modules <a name="modules"></a><a name="available-modules"></a>

*The 26 topics and their authors are listed here. If you would like guidance on what order to complete them in, jump to the recommended learning pathways in the next section.*

+ [Fundamentals of Bioinformatics](https://github.com/NIGMS/Fundamentals-of-Bioinformatics) - Dartmouth College ![Google Logo](images/google-cloud-small.png) ![AWS Logo](images/aws-small.png) ![Azure Logo](images/azure-small.png)
+ [DNA Methylation Sequencing Analysis with WGBS](https://github.com/NIGMS/DNA-Methylation-Sequencing-Analysis-with-WGBS) - University of Hawaii at Manoa
+ [Transcriptome Assembly Refinement and Applications](https://github.com/NIGMS/Transcriptome-Assembly-Refinement-and-Applications) - MDI Biological Laboratory
+ [RNAseq Differential Expression Analysis](https://github.com/NIGMS/RNA-Seq-Differential-Expression-Analysis) - University of Maine
+ [Proteome Quantification](https://github.com/NIGMS/Proteome-Quantification) - University of Arkansas for Medical Sciences
+ [ATAC-Seq and Single Cell ATAC-Seq Analysis](https://github.com/NIGMS/ATAC-Seq-and-Single-Cell-ATAC-Seq-Analysis) - University of Nebraska Medical Center
+ [Consensus Pathway Analysis in the Cloud](https://github.com/NIGMS/Consensus-Pathway-Analysis-in-the-Cloud) - University of Nevada Reno
+ [Integrating Multi-Omics Datasets](https://github.com/NIGMS/Integrating-Multi-Omics-Datasets) - University of North Dakota
+ [Metagenomics Analysis of Biofilm-Microbiome](https://github.com/NIGMS/Metagenomics-Analysis-of-Biofilm-Microbiome) - University of South Dakota
+ [Introduction to Data Science for Biology](https://github.com/NIGMS/Introduction-to-Data-Science-for-Biology) - San Francisco State University
+ [Analysis of Biomedical Data for Biomarker Discovery](https://github.com/NIGMS/Analysis-of-Biomedical-Data-for-Biomarker-Discovery) - University of Rhode Island
+ [Biomedical Imaging Analysis using AI/ML approaches](https://github.com/NIGMS/Biomedical-Imaging-Analysis-using-AI-ML-Approaches) - University of Arkansas

## Recommended Learning Pathways <a name="pathways"></a>

:sparkles: _We put together these learning pathways to help orient you to using the Sandbox modules. Before starting on any of the individual modules, we recommend you complete all the steps in the Prerequisites section for your respective cloud provider and only continue once you are able to check off these key skills._

**Prerequisites: Introduction to AWS**

**Prerequisites: Introduction to Azure**

**Prerequisites: Introduction to GCP**

   _Here are some GCP prerequisites you should make sure you can complete before diving into the modules. These will give you the necessary cloud computing skills to run the training modules such as launching a VM, cloning modules from GitHub, and more. If anything looks unfamiliar, follow the link to view documentation on that subject. After reading the documentation in the links below, complete the simple tasks described in the steps below as a knowledge check on what you just learned. Complete each step in order to learn the key skills you need to complete the learning modules in the next section!_
   - STEP 1: [Select your GCP Project](https://github.com/NIGMS/NIGMS-Sandbox/blob/main/docs/open_GCP_project.md)
   - STEP 2: [Navigate to Vertex AI and Launch an Instance](https://github.com/STRIDES/NIHCloudLabGCP/blob/main/docs/vertexai.md). Enable idle-shutdown after 15 minutes of inactivity.
   - STEP 3: [Change your Notebook Kernel](https://cloud.google.com/vertex-ai/docs/workbench/managed/create-managed-notebooks-instance-console-quickstart)
   - STEP 4: [Enable the Google Batch and Big Query APIs](https://cloud.google.com/apis/docs/getting-started#enabling_apis)
   - STEP 5: [Read our Billing Guide](https://github.com/STRIDES/NIHCloudLabGCP/blob/main/docs/How%20to%20Create%20Labels%20and%20GCP%20Billing%20Report.docx.pdf). Generate a billing report for the last 30 days.
   - STEP 6: Review [this overview](https://github.com/STRIDES/NIHCloudLabGCP/blob/main/docs/containers.md) of pushing and pulling containers. Try to spin up a Vertex AI notebook from this container path: `us-east4-docker.pkg.dev/nih-cl-shared-resources/nigms-sandbox/nvidiaforVertex AI-rapids-22.12-cuda11.5-runtime-ubuntu20.04-py3.9@sha256:bb6703315633f21281e8caceed811f74822564a63ede01953664fe8d58b0c658`. Review [these instructions](https://github.com/NIGMS/ATAC-Seq-and-Single-Cell-ATAC-Seq-Analysis) for help.
   - STEP 7: Clone this GitHub repository into a Vertex AI Notebook Instance using [the command line](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or the [Vertex AI user interface](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/save-to-github).
   - STEP 8: Review how to [open a GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue). If you have a question or a suggested enhancement, feel free to open an issue for this repository or for the module you are having trouble with. You can also email us at `CloudLab@nih.gov`.
   - STEP 9: Read over the [NIH Cloud Lab README](https://github.com/STRIDES/NIHCloudLabGCP/tree/main) to become familiar with additional Cloud services that may be needed during these modules. Pay special attention to Google Cloud Storage and Cost Optimization.

After completing this prerequisite learning path, you should be able to:
   + Navigate the GCP console
   + Use Vertex AI Notebook instances
   + Copy data to and from a Google Cloud Storage Bucket
   + Enable APIs
   + Understand Billing
   + Pull container images and launch an instance from a container
   + Use GitHub repositories.

:surfer: _You are now ready to start analyzing data!_

We have organized the rest of the learning pathways by scientific topic area and ordered them according to technical complexity within each pathway. Our ordering is only based on the number and complexity of cloud services used and has no bearing on the complexity of the scientific content. We recommend you being with Introductory modules within a given scientific interest area, and then progress to the more advanced modules as you gain key skills. 
+ Introductory modules :seedling: use only Jupyter notebooks and sometimes Cloud Storage. Upon completion, users should be comfortable starting a Jupyter notebook instance and with copying data to and from Cloud Storage. 
+ Advanced modules :deciduous_tree: include additional functionality such as launching a notebook from a custom Docker container, making API calls from with the notebook to Batch Computing, and using GPU-enabled machine types. Upon completion of advanced modules, users should be comfortable interacting with additional cloud services from within the Jupyter interface.

**Introduction to Biomedical Data Science**
   + :seedling: [Fundamentals of Bioinformatics](https://github.com/NIGMS/Fundamentals-of-Bioinformatics) - Dartmouth College
   + :seedling: [Introduction to Data Science for Biology](https://github.com/NIGMS/Introduction-to-Data-Science-for-Biology) - San Francisco State University
   + :seedling: [Introduction to Python for Biology]() - Northern Nazarene University
   + :seedling: [Introduction to R and LLMs for Biology]() - Duke University

*After completing this learning path, you should be able to conduct comprehensive data science analysis with a variety of bioinformatics data sources. Your skills now include version control and creating reproducible workflows, downloading, processing, and visualizing data, calculating statistically significant variables, using GenAI chatbots, and building and evaluating machine learning models with real biomedical data.*

*After completing this learning path, you will gain proficiency in cloud computing and storage, master the Linux command line and BASH scripting for bioinformatics workflowsm, and learn to preprocess and manage biomedical datasets using Python, R, and BASH. You will also learn introduction to genomic analysis, develop and evaluate machine learning models for biomedical applications, and learn data visualization.*

| Specs                    |      Details     |
|--------------------------|------------------|
| Languages and Workflows  | Python, R, BASH  |
| Jupyter Notebooks        | 36               |
| Approximate Cost         | $17.00           |


**Introduction to Biomedical Machine Learning and Artificial Intelligence**
   + :seedling: [Python and ML for Biomedical Data Science]() - University of Delaware
   + :seedling: [Analysis of Biomedical Data for Biomarker Discovery](https://github.com/NIGMS/Analysis-of-Biomedical-Data-for-Biomarker-Discovery) - University of Rhode Island
   + :deciduous_tree: [Biomedical Imaging Analysis using AI/ML approaches](https://github.com/NIGMS/Biomedical-Imaging-Analysis-using-AI-ML-Approaches) - University of Arkansas

*After completing this learning path, you should understand and apply the data science lifecycle and FAIR data principles, develop ethical AI/ML systems and interpret model decisions, prepare biomedical datasets by preprocessing managing and augmenting data, and implement deep learning methods including transfer learning and models. You will also learn to perform statistical analyses, utilize dimensionality reduction techniques on high-dimensional biomedical data, evaluate model performance, and improve models by addressing biomedical-specific data challenges.*

| Specs                    |      Details     |
|--------------------------|------------------|
| Languages and Workflows  | Python, R        |
| Jupyter Notebooks        | 60               |
| Approximate Cost         | $30.00           |

**Introduction to Biomedical Genomics**
   + :seedling: [Consensus Pathway Analysis in the Cloud](https://github.com/NIGMS/Consensus-Pathway-Analysis-in-the-Cloud) - University of Nevada Reno
   + :deciduous_tree: [DNA Methylation Sequencing Analysis with WGBS](https://github.com/NIGMS/DNA-Methylation-Sequencing-Analysis-with-WGBS) - University of Hawaii at Manoa
   + :deciduous_tree: [ATAC-Seq and Single Cell ATAC-Seq Analysis](https://github.com/NIGMS/ATAC-Seq-and-Single-Cell-ATAC-Seq-Analysis) - University of Nebraska Medical Center
   + :deciduous_tree: [Chromatin Occupancy with Cut and Run]() - University of Nebraska Medical Center
   + :deciduous_tree: [Integrating Multi-Omics Datasets](https://github.com/NIGMS/Integrating-Multi-Omics-Datasets) - University of North Dakota

*After completing this learning path, you should be able to manage and analyze large genomic and omics datasets using cloud computing, perform quality control and become facile with Nextflow pipelines, conduct and interpret differential analyses, and visualize multi-omics datasets to derive biological insights. You will also apply statistical methods and computational tools for genomic analysis, and retrieve and manage data from biological databases.*

| Specs                    |      Details     |
|--------------------------|------------------|
| Languages and Workflows  | BASH, R, Nextflow|
| Jupyter Notebooks        | 22               |
| Approximate Cost         | $14.00           |

**Introduction to Metagenomics and Phylogenetics**
   + :seedling: [Introduction to Amplicon-based Metagenomics]() - University of Nevada Reno
   + :seedling: [Introduction to Phylogenetics]() - University of South Dakota
   + :seedling: [Introduction to Population Genomics]() - University of Wyoming
   + :deciduous_tree: [Comparative Prokaryotic Genomics]() - University of New Hampshire
   + :deciduous_tree: [Introduction to Pangenomic Methods]() - National Center for Genome Resources
   + :deciduous_tree: [Metagenomics Analysis of Biofilm-Microbiome](https://github.com/NIGMS/Metagenomics-Analysis-of-Biofilm-Microbiome) - University of South Dakota

*After completing this learning path, you should know how to analyze microbial data to perform taxonomic classification using diversity and differential abundance analyses, utilize comparative genomics and phylogenetics to interpret genome sequences and evolutionary relationships, and implement cloud-based bioinformatics workflows including pipeline configuration resource scheduling and scalable analysis. Further, you will be able to access, retrieve, and manage genomic data from biological databases and sequencing sources, assemble, annotate, and analyze genome sequences utilizing bioinformatics tools and cloud resources, and apply quality control techniques and standardized bioinformatic data processing workflows for reproducibility. Finally, you will be able to visualize genomic, metagenomic, and microbial community data, relate genomic microbial and phylogenetic findings to metadata geographic context and biological interpretation, and leverage machine learning with comparative genomics and population genomics in genomic analyses and pangenome studies.*

| Specs                    |      Details     |
|--------------------------|------------------|
| Languages and Workflows  | BASH, R, Nextflow|
| Jupyter Notebooks        | 29               |
| Approximate Cost         | $22.00           |

**Introduction to Proteomics**

   + :seedling:[Proteome Quantification](https://github.com/NIGMS/Proteome-Quantification) - University of Arkansas for Medical Sciences
   + :seedling:[Proteome Structures and Docking](https://github.com/NIGMS/Proteome-Quantification) - University of Arkansas for Medical Sciences
   + :seedling:[Proteome Quantification](https://github.com/NIGMS/Proteome-Quantification) - University of Arkansas for Medical Sciences
   + :seedling:[Proteome Quantification](https://github.com/NIGMS/Proteome-Quantification) - University of Arkansas for Medical Sciences


After completing this learning path, you should be comfortable analyzing bioinformatics data on the command line in a cloud environment and integrating -omics data to understand biological insight. These skills can be applied to a wide variety of Omics datasets in the subsequent sections.
     
**Introduction to Genomic Analysis**

After completing this learning path, you now have experience with specialized genomics and metagenomics analysis. These tools differ from standard Omics analysis in the highly specialized tools they use, which you can now deploy in a GCP environment.
     
**Introduction to RNAseq and Transcriptome Assembly**
   + :deciduous_tree: [RNAseq Differential Expression Analysis](https://github.com/NIGMS/RNA-Seq-Differential-Expression-Analysis) - University of Maine
   + :deciduous_tree: [Transcriptome Assembly Refinement and Applications](https://github.com/NIGMS/Transcriptome-Assembly-Refinement-and-Applications) - MDI Biological Laboratory

After completing this learning path, you are able to do a full analysis of RNA-seq data, including assembling a transcriptome and identifying differentially expressed genes. These are computationally intensive tools which the Cloud enables you to conduct in a scalable manner. 

_That concludes our section on Learning Pathways. The rest of the README will walk you through some of the technical details of each module, in particular focusing on compute environments and machine types, as well as additional resources to help you continue your learning journey!_

