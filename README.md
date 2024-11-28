# Implementing and Evaluating End-to-End Differential Privacy Frameworks
This is an end-to-end framework to evaluate and implement differential privacy 

## Differntial Privacy

Differential privacy allows privacy-preserving analysis by adding carefully calibrated noise.  It provides a mathematical framework for releasing statistical results about a dataset
It enables the data holder to publish aggregate statistics without revealing information about any individual. The noise is injected in a way that preserves the utility (accuracy) of the 
results. 

### Differntial Privacy Models
There are mainly two differential privacy models central differential privacy (CDP) and local differential privacy (LDP) the widely used mode is CDP to implement in differential privacy. A friendly and non-technical blog to know about differential privacy and a few implementations of differential privacy by industry [A friendly, non-technical introduction to differential privacy](https://desfontain.es/blog/friendly-intro-to-differential-privacy.html). 

### Introduction
The repository implements various experiments and analyses focused on central differential privacy. It explores various features and matrices to evaluate and implement differential privacy rigorously in terms of real-world implementation. 
In this work, we have proposed a framework with a set of matrices to evaluate and implement CDP without having detailed knowledge about Dp. 
The work addresses various misconceptions and questions while implementing differential privacy such as:

 *  How to do sensitivity analysis
 *  Which noise mechanism to choose (Laplace or Gaussian)
 *  The behaviour of noise mechanism when used in a real-world setting
 *  The effect of privacy budget and accuracy using a different mechanism
 *  Set of matrices to implement a differential private framework (Threshold bounds, epsilon sensitivity index, Type errors, Relative Error, Absolute Difference and Accuracy )
 *  How to select an epsilon for a particular use case with balancing privacy vs utility trade-off

# Implementation
The framework is an end-to-end framework designed to be used by all users without having expertise in differential privacy allowing the user to evaluate DP mechanism and how they can execute queries in order to publish statistics. The framework is implemented using Python and widely familiar libraries such as Pandas and NumPy to generate noise from Laplace and Gaussian distribution. The repository consists of the following scripts 
* Sensitivity analysis: count sensitivity, sum sensitivity and average
* Adding Noise to the queries tailored to the sensitivity of the query being executed
* Evaluation of privacy budget concerning noise mechanism, privacy vs utility tradeoff and other discussed matrices
* Generating graphs and publishing the statistics

## How to Use

* Upload your dataset 
* Open the desired sensitivity analysis file to perform sensitivity analysis for the desired query. 
* Open the desired noise adding file such as 'Noise-count'
* Enter the sensitivity for the query and select the query
* Analyse the DP matrices and analyse it with your dataset
