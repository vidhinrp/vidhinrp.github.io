# Hi there, I'm Vidhi. 

Below are some data science projects I've recently worked on.

## Machine Learning Reports

### GFlowNet Graph Neighbor Sampling For Link Prediction
[Paper]()
[Code](https://github.com/vidhinrp/CPSC583)
Graph Neural Networks (GNNs) are powerful for representation learning but face scalability challenges in handling complex node connectivity. To address [this](https://arxiv.org/pdf/2310.03399.pdf) GFlowNet Graph Neighbor Sampling (GRAPES) was introducted as an adaptive solution that maximizes GNN  accuracy within a fixed sampling budget amd was tested on node classification tasks. I extended this sampling solution to link prediction tasks, including negative edge sampling in GCN training. The results are promising, with GRAPES performing competitively or better than state-of-the-art methods on standard datasets (Cora and CiteSeer) across various sample sizes.

## Python

### Classification: Predicting Hospital Admission Based on Emergency Admission Triage

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Titanic.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Titanic.ipynb)

Using patient history data (900+ features and 500K+ entries) from three EDs - a level I trauma center, a community hospital-based department, and a suburban, free-standing department - collected between March 2013 to July 2017, I attempted to recreate and extend explainability of results from an existing [study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0201016#sec005). The study aimed to predict hospital admission at the time of triage in the emergency department. Accuracy in comparison to the orignal paper of logistic regression (83% vs 87%) and XGBoost (85% vs 87% accurary) models was within reason. I further examined inner-workings of models using SHAP values. 

### Natural Language Processing: Fine-tuning BART For Text Summarization

[Github]() 
[Notebook]()

Using BART (Bidirectional and Auto-Regressive Transformers) to conduct text summarization, implemented custom cross-entropy loss and ROUGE-based performance evaluation functions. Additionally, tested multiple decoding algorithms including greedy decoding, BEAM search and sampling. Tested performanceo on XSum dataset. 

### Simulation: Optimizing Therapy for Pediatric Asthma: Daily vs. Intermittent ICS

[Github]() 
[Paper]().
Assessed cost-effectiveness of two types of pediatric asthma therapies (daily or intermittent) in Colombia using discrete-time Markov chain. Looked at cost per patient and average health utility for each therapy to determine the optimal therapy is daily ICS, yielding a cost-savings of $152/patient. Conducted sensitvity analysis by simulating 1000 cohorts using monte carlo techniques, helping highlight the robustness of initial model results. 

### Simulation: Discrete Event Urgent Care Simulation

[Github]()

Developed a discrete event simulation model for an urgent care facility to optimize operational efficiency by tracing patient waiting times for various services. 

### Data Analysis: Armed Water Conflicts

[Notebook ]()

Using data from the Pacific Institute, conducted data analysis on armed conflicts associated with water resources and water systems, as identified from news reports, eyewitness accounts, and other conflict databases.

## R

### Survival Analysis: Time-Dependent Cox Model Analysis

[Github]()
[Report]()

Recreated select analyses from John Crawley and Marie Hu's paper Covariance Analysis of Heart Transplant Survival Data. Evaluated effects of time-varying covariates on survival of transplant by looking at parameter estimations of three seperate Cox proportional hazard models. Looked at estimations of relative risk of transplants for age-varying groups using a selected model from those evaluated. 

