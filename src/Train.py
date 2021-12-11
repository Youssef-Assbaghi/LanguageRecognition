# -*- coding: utf-8 -*-
"""
@author: Youssef
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier

class Train(object):
    
    def NaiveBayes(self,x_train,y_train):
        print("Naive Bayes ")
        model = MultinomialNB()
        model.fit(x_train, y_train)
        return model
        
        
    def MultiLayerPerceptron(self,x_train,y_train):
        print("Multi Layer Perceptron ")
        clf = MLPClassifier(solver='adam', alpha=0.001,
                            hidden_layer_sizes=(10,), random_state=1,warm_start=True)
        
        clf.fit(x_train, y_train)
        return clf
        
    def StochaisticGradientDescent(self,x_train,y_train):
        print("Stochaistic Gradient Descent ")
        model1=SGDClassifier(loss='hinge', penalty='l2',alpha=0.001, random_state=42,max_iter=1000, tol=None)
        model1.fit(x_train, y_train)
        return model1
        
    def RandomForest(self,x_train,y_train):
        print("Random Forest ")
        clf = RandomForestClassifier(max_depth=1000, random_state=0)
        clf.fit(x_train, y_train)
    
        return clf
        
    