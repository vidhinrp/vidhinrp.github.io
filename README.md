
# Hi there, I'm Vidhi. 

Below are some data science projects I've recently worked on.

## Machine Learning Reports

### GFlowNet Graph Neighbor Sampling For Link Prediction

[Paper](https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/grapes.pdf)
[Code](https://github.com/vidhinrp/CPSC583)

Graph Neural Networks (GNNs) are powerful for representation learning but face scalability challenges in handling complex node connectivity. To address [this](https://arxiv.org/pdf/2310.03399.pdf) GFlowNet Graph Neighbor Sampling (GRAPES) was introducted as an adaptive solution that maximizes GNN  accuracy within a fixed sampling budget amd was tested on node classification tasks. I extended this sampling solution to link prediction tasks, including negative edge sampling in GCN training. The results are promising, with GRAPES performing competitively or better than state-of-the-art methods on standard datasets (Cora and CiteSeer) across various sample sizes.

## Python

### Classification: Predicting Hospital Admission Based on Emergency Admission Triage

[Notebook](https://htmlpreview.github.io/?https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/admissionstatus.html) 

Using patient history data (900+ features and 500K+ entries) from three EDs - a level I trauma center, a community hospital-based department, and a suburban, free-standing department - collected between March 2013 to July 2017, I attempted to recreate and extend explainability of results from an existing [study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0201016#sec005). The study aimed to predict hospital admission at the time of triage in the emergency department. Accuracy in comparison to the orignal paper of logistic regression (83% vs 87%) and XGBoost (85% vs 87% accurary) models was within reason. I further examined inner-workings of models using SHAP values. 

### Natural Language Processing: Fine-tuning BART For Text Summarization

[Notebook](https://htmlpreview.github.io/?https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/textsummarization.html)

Using BART (Bidirectional and Auto-Regressive Transformers) to conduct text summarization, I implemented custom cross-entropy loss and ROUGE-based performance evaluation functions. Additionally, I tested multiple decoding algorithms including greedy decoding, BEAM search and sampling. The performance of the model was evaluated on the XSum dataset. 

### Simulation: Optimizing Therapy for Pediatric Asthma: Daily vs. Intermittent ICS

[Github]() 
[Paper](https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/costeffectiveness.pdf).

I assessed cost-effectiveness of two types of pediatric asthma therapies (daily or intermittent) in Colombia using discrete-time Markov chain. Looked at cost per patient and average health utility for each therapy to determine the optimal therapy is daily ICS, yielding a cost-savings of $152/patient. I conducted sensitvity analysis by simulating 1000 cohorts using Monte Carlo techniques, helping highlight the robustness of initial model results. 

### Simulation: Discrete Event Urgent Care Simulation

[Github](https://github.com/vidhinrp/urgentcaresim)

I developed a discrete event simulation model for an urgent care facility to optimize operational efficiency by tracing patient waiting times for various services. 

### Data Analysis: Armed Water Conflicts

[Notebook](https://htmlpreview.github.io/?https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/waterconflicts.html)

Using data from the Pacific Institute, I conducted data analysis on armed conflicts associated with water resources and water systems, as identified from news reports, eyewitness accounts, and other conflict databases.

## R

### Survival Analysis: Time-Dependent Cox Model Analysis

[Github]()
[Report](https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/transplant_survival.pdf)

Recreated select analyses from John Crawley and Marie Hu's paper Covariance Analysis of Heart Transplant Survival Data. I evaluated effects of time-varying covariates on survival of transplant by looking at parameter estimations of three seperate Cox proportional hazard models. I looked at estimations of relative risk of transplants for age-varying groups using a selected model from those evaluated. 

### Longitudinal and Multilevel Modeling: Assessing Arthritis Treatment Efficacy

[R Markdown](https://github.com/vidhinrp/vidhipatel.github.io/blob/1f27c629601bfe296ca646b787fffaf9f27b1ef9/Projects/arthiritis_glmm.pdf)

Using a dataset from a clinical trial comparing auranofin therapy and placebo for the treatment of rheumotoid arthiritis, I used Generalized Linear Mixed Models (GLMM) and Multinomial Generalized Linear Models (MGLM) to predict arthritis severity over a 6-month post-treatment period. I further evaluated the models by conducting hypothesis testing to assess significance of random effects and intervention effects within models. Examined robustness of best performing model using data visualizations like probability estimation plot, odds-ratio plot and cumulative log-odds plot. 

### Data Analysis and Regression Modeling: Assessing Key Drivers of Birthweight

[Github]()
[Report](https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/birthweight_regression.pdf)

Aimed to understand and predict Low Birth Weight (LBW) by analyzing an anoynomized dataset. Through rigorous data cleaning, normalization, and advanced regression techniques, including hybrid forward-backward stepwise and ridge regression, key variables influencing birth weight were identified. Factors such as mother's pre-pregnancy weight, birth head circumference, number of prior live births, and parental races emerged as significant, though limitations exist due to unknown population origin in the dataset. 

## PySpark/Spark

### ETL: Patient Data

[Github](https://github.com/vidhinrp/vidhipatel.github.io/tree/77f5af1e82c864c5b2aa077bcc3f2bc79cffc70d/patient_records)
[Notebook](https://htmlpreview.github.io/?https://github.com/vidhinrp/vidhipatel.github.io/blob/bfeffc0000eacb49cd16fb468c2c1725975b5c40/Projects/patient_records.html)

Using synthetic patient data from the Synthea database that was adopted to fit the OMOP schema, created PySpark scripts to extract, load and transform relevant patient information. The scripts extract data from tables stored on AWS related to demographic information, medical measurements, and medical conditions. Variables were transformed to ensure standardization and then loaded into singular dataframe based on dataset requirements. Demonstrated how the scripts work and final dataframe generation as well as generated plots to visualize final data in the notebook above.
