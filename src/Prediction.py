# -*- coding: utf-8 -*-
"""
@author: Youssef
"""
from sklearn.metrics import f1_score

class Prediction(object):
    
    def predict(self,clf,x_test,y_test):
        y_pred=clf.predict(x_test)
        self.plot_F_Scores(y_test,y_pred)
        
        
    def plot_F_Scores(self,y_test, y_predict):
        f1_micro = f1_score(y_test, y_predict, average='micro')
        f1_macro = f1_score(y_test, y_predict, average='macro')
        f1_weighted = f1_score(y_test, y_predict, average='weighted')
        print("F1: {} (micro), {} (macro), {} (weighted)".format(f1_micro, f1_macro, f1_weighted))