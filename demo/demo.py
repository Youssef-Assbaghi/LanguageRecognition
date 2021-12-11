# -*- coding: utf-8 -*-
"""
@author: Youssef
"""
import pickle

if __name__ == '__main__':
    
    print("Write a sentece or a word: ")
    #MLP
    texto=input()
    texto=[texto]
    filename="../models/MLP.pkl"
    with open(filename, 'rb') as f:
        count_vect, clf = pickle.load(f)
    texto=count_vect.transform(texto)
    prediction=clf.predict(texto)
    print("The language predicted by MLP is ",prediction[0])
    
    filename="../models/NaveBayes.pkl"
    with open(filename, 'rb') as f:
        count_vect, clf = pickle.load(f)
    prediction=clf.predict(texto)
    print("The language predicted by Multinomial Naive Bayes is ",prediction[0])
    
    filename="../models/RandomForest.pkl"
    with open(filename, 'rb') as f:
        count_vect, clf = pickle.load(f)
    prediction=clf.predict(texto)
    print("The language predicted by RandomForest is ",prediction[0])
    
    filename="../models/SGD.pkl"
    with open(filename, 'rb') as f:
        count_vect, clf = pickle.load(f)
    prediction=clf.predict(texto)
    print("The language predicted by SGD is ",prediction[0])
