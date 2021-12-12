# LanguageRecognition

 This is a project of the machine learning course and is based on recognizing the language in which a text is written. To validate the results you can run the demo.py file and see the results of a text for each model.



# Table of Contents
 
 <img src="https://miro.medium.com/max/960/0*xLRsbQ02J7sQpNNy" align="right" width="300" alt="header"/>

   * [What is this?](#1)
   * [Requeriments](#R)
   * [Description](#2)
      * [Language](#7)
   * [Models](#3)
   * [Results](#4)


   * [Authors](#6)



# What is this? <a name="1"></a>
Recognize the situations in which the application of computational learning algorithms can be useful to solve a problem.
can be useful to solve a problem.Analyze the problem to be solved and design the optimal solution by applying the techniques learnt. Write technical documents related to the analysis and solution of a problem. Program the basic algorithms to solve the proposed problems. Evaluate the results of the implemented solution and assess possible improvements and defend and argue the decisions taken in the solution of the proposed problems.


# Requeriments <a name="R"></a>
For running each sample code:

- <a href="https://www.python.org/downloads/">Python 3.7</a>

- <a href="https://numpy.org/install/">numpy</a>

- math
- Jupyter Notebook

- matplotlib

- <a href="https://scikit-learn.org/stable/install.html">sklearn</a>

- seaborn
- <a href="https://git-lfs.github.com/"> Git LFS </a>ç

## RUN DEMO:
1. Install Git LFS
2. Install python3
3. Install sklearn
4. Clone this repo (Importat to have step 1)
5. Run file demo.py
6. Write a sentence or a text
7. See predictions!


# Description <a name="2"></a>
 
  In order to make a good language prediction, we must first follow a series of steps to ensure that we do it correctly:
  - Load the data
  - Convert the dataset to lowercase
  - Verify that there are no null rows, if there are, remove them from the dataset.
  - Separate the dataset into training and test subsets.
  - Convert the training and test data into a sparse matrix with the CountVectorizer function.
  - Test different models

As we can see we have the same number of datasets for each language this makes mor easier to split the dataset to train and test.
![image](https://user-images.githubusercontent.com/72655367/145685007-72932db1-8459-4a2d-8e36-8bb74640448b.png)


## Loading the data <a name="7"></a>
WiLI-2018, the Wikipedia language identification benchmark dataset, contains 235000 paragraphs of 235 languages. Each language in this dataset contains 1000 rows/paragraphs.

We use a dataset that contains 22 selective languages from the original dataset which includes the following Languages
  -  English
  -  Arabic
  -  French
  -  Hindi
  -  Urdu
  -  Portuguese
  -  Persian
  -  Pushto
  -  Spanish
  -  Korean
  -  Tamil
  -  Turkish
  -  Estonian
  -  Russian
  -  Romanian
  -  Chinese
  -  Swedish
  -  Latin
  -  Indonesian
  -  Dutch
  -  Japanese
  -  Thai

# Models <a name="3"></a>
In this project i had to use a classifier. Because of that i tried different models to select the best ones.
The models that were used in this project were the next ones: Multinomial Naive Bayes, Stochaistic Gradient Descent Classifier, Decision Tree Classifier with both criterion (gini and entropy), K-Neighbors Classifier, Support Vector Machine with the kernels of (rbf and poly), Random Forest Classifier and the Multi Layer Perceptron.

Comparing the different results I have realized that the best algorithms are Naive Bayes, Random Forest and Multi Layer Perceptron. This is due to the fact that I have as success criterion a precision higher than 90%.Furthermore, by improving the hyperparameters of the Decision Tree algorithms, we will probably reach an accuracy similar to that of the Random Forest, but due to time constraints it has not been possible to verify it.


# Results <a name="4"></a>
As can be seen in the graph the best algorithms for classifying languages are gradient descent and Multi Layer Perceptron. These two give an accuracy of more than 96%.

| Algorithm/score              | F1 (micro)           | F1 (macro)         | F1 (weighted)   |
|------------------------------|----------------------|--------------------|-----------------|
| Naive Bayes                  |       0,944393939    |        0,941980548 |     0,943844696 | 
| Stochaistic Gradient Descent |       0,966212121    |        0,966096163 |     0,966676063 | 
| Random Forest                |       0,947059245    |        0,947059245 |      0,94784544 |
| Multi Layer Perceptron       |       0,963030303    |        0,962499506 |     0,963192635 |
| Decision Tree Entropy        |       0,890454545    |        0,893456212 |     0,898740202 |
| Decision Tree Gini           |       0,884242423    |        0,887271508 |     0,888739760 |


<img src="https://github.com/Youssef-Assbaghi/LanguageRecognition/blob/main/demo/Grafcos.png"  alt="header"/>

# Authors <a name="6"></a>
Youssef Assbaghi 1493477 UAB
