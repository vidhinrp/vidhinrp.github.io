# Hi there, I'm Vidhi. 

Below are some data science projects I've recently worked on.

## Machine Learning Reports

### GFlowNet Graph Neighbor Sampling For Link Prediction
[Paper]()
[Code](https://github.com/vidhinrp/CPSC583)
Graph Neural Networks (GNNs) are powerful for representation learning but face scalability challenges in handling complex node connectivity. To address [this](https://arxiv.org/pdf/2310.03399.pdf) GFlowNet Graph Neighbor Sampling (GRAPES) was introducted as an adaptive solution that maximizes GNN  accuracy within a fixed sampling budget amd was tested on node classification tasks. I extended this sampling solution to link prediction tasks, including negative edge sampling in GCN training. The results are promising, with GRAPES performing competitively or better than state-of-the-art methods on standard datasets (Cora and CiteSeer) across various sample sizes.

## Python

### Predicting Hospital Admission Based on Emergency Admission Triage

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Titanic.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Titanic.ipynb)

Using patient history data (900+ features and 500K+ entries) from three EDs - a level I trauma center, a community hospital-based department, and a suburban, free-standing department - collected between March 2013 to July 2017, I attempted to recreate and extend explainability of results from an existing [study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0201016#sec005). The study aimed to predict hospital admission at the time of triage in the emergency department. Accuracy in comparison to the orignal paper of logistic regression (83% vs 87%) and XGBoost (85% vs 87% accurary) models was within reason. I further examined inner-workings of models using SHAP values. 

### Ghouls, Goblins, and Ghosts... Boo!

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/GGG.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/GGG.ipynb)

Ghouls, Goblins, and Ghosts... Boo! is a knowledge competition on Kaggle. This is a multiple classification problem: based on information about monsters we predict their types. A fun competition for Halloween. General description and data are available on [Kaggle](https://www.kaggle.com/c/ghouls-goblins-and-ghosts-boo).
This dataset has little number of samples, so careful feature selection and model ensemble are necessary for high accuracy.

### Otto Group Product Classification Challenge

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Otto_Group.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Otto_Group.ipynb)

Otto Group Product Classification Challenge is a knowledge competition on Kaggle. This is a multiple classification problem. Based on information about products we predict their category. General description and data are available on [Kaggle](https://www.kaggle.com/c/otto-group-product-classification-challenge).
The data is obfuscated, so the main questionlies in the selection of the model for prediction.

### Imbalanced classes

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Imbalanced.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Imbalanced.ipynb)

In real world it is common to meet data in which some classes are more common and others are rarer. In case of a serious disbalance prediction rare classes could be difficult using standard classification methods. In this notebook I analyse such a situation. I can't share the data, used in this analysis.

### Bank card activations

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Card_activation.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Card_activation.ipynb)

Banks strive to increase the efficiency of their contacts with customers. One of the areas which require this is offering new products to existing clients (cross-selling). Instead of offering new products to all clients, it is a good idea to predict the probability of a positive response. Then the offers could be sent to those clients, for whom the probability of response is higher than some threshold value.
In this notebook I try to solve this problem.

## Regression problems.

### House Prices: Advanced Regression Techniques

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/House_Prices.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/House_Prices.ipynb)

House Prices: Advanced Regression Techniques is a knowledge competition on Kaggle. This is a regression problem: based on information about houses we predict their prices. General description and data are available on [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).
The dataset has a lot of features and many missing values. This gives interesting possibilities for feature transformation and data visualization.

### Loan Prediction

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Loan_Prediction.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Loan_Prediction.ipynb)

Loan Prediction is a knowledge and learning hackathon on Analyticsvidhya. Dream Housing Finance company deals in home loans. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. Based on customer's information we predict whether they should receive a loan or not. General description and data are available on [Analyticsvidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/).


### Caterpillar Tube Pricing

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Caterpillar.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Caterpillar.ipynb)

Caterpillar Tube Pricing is a competition on Kaggle. This is a regression problem: based on information about tube assemblies we predict their prices. General description and data are available on [Kaggle](https://www.kaggle.com/c/caterpillar-tube-pricing).
Dataset consists of many files, so there is an additional challenge in combining the data snd selecting the features.

## Natural language processing.

### Bag of Words Meets Bags of Popcorn

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Bag_of_Words.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Bag_of_Words.ipynb)

Bag of Words Meets Bags of Popcorn is a sentimental analysis problem. Based on texts of reviews we predict whether they are positive or negative. General description and data are available on [Kaggle](https://www.kaggle.com/c/word2vec-nlp-tutorial).
The data provided consists of raw reviews and class (1 or 2), so the main part is cleaning the texts.

### NLP with Python: exploring Fate/Zero

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Fate_Zero_explore.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Fate_Zero_explore.ipynb)

Natural language processing in machine learning helps to accomplish a variety of tasks, one of which is extracting information from texts. This notebook is an overview of several text exploration methods using English translation of Japanese light novel "Fate/Zero" as an example.

### NLP. Text generation with Markov chains

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Markov_chain_nlp.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Markov_chain_nlp.ipynb)

This notebook shows how a new text can be generated based on a given corpus using an idea of Markov chains. I start with simple first-order chains and with each step improve model to generate better text.

### NLP. Text summarization

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Summarize.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Summarize.ipynb)

This notebook shows how text can be summarized choosing several most important sentences from the text. I explore various methods of doing this based on a news article.

## Clustering

### Clustering with KMeans

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Clustering_with_K-Means.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Clustering_with_K-Means.ipynb)

Clustering is an approach to unsupervised machine learning. Clustering with KMeans is one of algorithms of clustering. in this notebook I'll demonstrate how it works. Data used is about various types of seeds and their parameters. It is available [here](https://archive.ics.uci.edu/ml/datasets/seeds).

## Neural networks

### Feedforward neural network with regularization

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/NN_GGG.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/NN_GGG.ipynb)

This is a simple example of feedforward neural network with regularization. It is based on Andrew Ng's lectures on Coursera. I used data from Kaggle's challenge "Ghouls, Goblins, and Ghosts... Boo!", it is available [here](https://www.kaggle.com/c/ghouls-goblins-and-ghosts-boo).

## Data exploration and analysis

### Telematic data

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Devices_analysis.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Devices_analysis.ipynb)

I have a dataset with telematic information about 10 cars driving during one day. I visualise data, search for insights and analyse the behavior of each driver. I can't share the data, but here is the notebook. I want to notice that folium map can't be rendered by native github, but nbviewer.jupyter can do it.

## Recommendation systems.

### Collaborative filtering

[Github](https://github.com/Erlemar/Erlemar.github.io/blob/master/Notebooks/Collaborative_filtering.ipynb) [nbviewer](http://nbviewer.jupyter.org/github/Erlemar/Erlemar.github.io/blob/master/Notebooks/Collaborative_filtering.ipynb)

Recommenders are systems, which predict ratings of users for items. There are several approaches to build such systems and one of them is Collaborative Filtering. 
This notebook shows several examples of collaborative filtering algorithms.
