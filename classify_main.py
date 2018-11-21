from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import numpy as np


#import matplotlib.pyplot as plt
#from __future__ import division  

train_data_path = './app_data/brexit/brexit_train_data.txt'
train_labels_path = './app_data/brexit/brexit_train_labels.txt'
test_data_path = './app_data/brexit/brexit_test_data.txt'
test_labels_path = './app_data/brexit/brexit_test_labels.txt'


#Training Data
with open(train_data_path, "r", encoding="utf-8") as f:
    x_train = f.readlines()
x_train = [m.strip() for m in x_train]
#Training Label
with open(train_labels_path, "r", encoding="utf-8") as f:
    labels_train = f.readlines()
labels_train = [m.strip() for m in labels_train]
#Testing Data
with open(test_data_path, "r", encoding="utf-8") as f:
    x_test = f.readlines()
x_test = [m.strip() for m in x_test]
#Testing Label
with open(test_labels_path, "r", encoding="utf-8") as f:
    labels_test = f.readlines()
labels_test= [m.strip() for m in labels_test]

#Bag-of-Words Matrix using TD-IDF instead of count. Shape is [n_samples, n_features]
tf = TfidfVectorizer()
x_train_tfidf = tf.fit_transform(x_train)

#Fit naiive bayes using training matrix and class vector
text_clf = MultinomialNB().fit(x_train_tfidf, labels_train)

#Accuracy using test set
x_test_tfidf = tf.transform(x_test)
predicted = text_clf.predict(x_test_tfidf)
print(np.mean(predicted == labels_test))


text_clf2 = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=6, random_state=42)
text_clf2 = text_clf2.fit(x_train_tfidf, labels_train)
predicted2 = text_clf2.predict(x_test_tfidf)
print(np.mean(predicted2 == labels_test))


#https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a


