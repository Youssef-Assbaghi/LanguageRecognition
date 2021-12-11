import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns # plotting

from sklearn.feature_extraction.text import CountVectorizer
from Train import Train
from Prediction import Prediction

def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset

def lower(dataset):
    return dataset.applymap(str.lower)



def plot_histogram(dataset):
    plt.figure(figsize=(10,10))
    plt.title('Language Counts')
    ax = sns.countplot(y=dataset['language'], data=dataset)
    plt.show()

def plot_count_languages():
    plt.figure(figsize=(10,10))
    plt.title('Language Counts')
    ax = sns.countplot(y=dataset['language'], data=dataset)
    plt.show()

def split_Datset(dataset):
    x_train, x_test, y_train, y_test = train_test_split(dataset.Text, dataset.language, test_size = 0.30)
    return x_train, x_test, y_train, y_test

def vectorize(x_test,x_train):
    count_vect = CountVectorizer(analyzer='word')
    x_train = count_vect.fit_transform(x_train)
    x_test=count_vect.transform(x_test)
    return x_train,x_test
        
if __name__ == '__main__':
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    # Carreguem dataset d'exemple
    dataset = load_dataset('./archives/dataset.csv')
    dataset=lower(dataset)
    x_train, x_test, y_train, y_test=split_Datset(dataset)
    x_train,x_test=vectorize(x_test, x_train)
    var=Train()
    prediction=Prediction()
    
    #NaiveBayes
    clf=var.NaiveBayes(x_train,y_train)
    prediction.predict(clf,x_test,y_test)
    
    #Stochaistic Gradient Descent
    clf=var.StochaisticGradientDescent(x_train,y_train)
    prediction.predict(clf,x_test,y_test)
    
    #Random Forest
    clf=var.RandomForest(x_train,y_train)
    prediction.predict(clf,x_test,y_test)
    
    #Multi Layer Perceptron
    clf=var.MultiLayerPerceptron(x_train,y_train)
    prediction.predict(clf,x_test,y_test)
    
    

