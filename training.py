
# coding: utf-8

# In[1]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import json
from sklearn.tree import _tree
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# In[2]:


dataset = pd.read_csv("data.csv")
data = np.array(dataset)

print('The dataset has {0} datapoints with {1} features'.format(data.shape[0], data.shape[1]-1))
#print('Features: {0}'.format([feature[0] for feature in dataset['attributes']]))


# In[19]:


data = data[:, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 23,30,31]]


# In[20]:


X, y = data[:, :-1], data[:, -1]
y.reshape(y.shape[0])
print('Before spliting')
print('X:{0}, y:{1}'.format(X.shape, y.shape))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
print('After spliting')
print('X_train:{0}, y_train:{1}, X_test:{2}, y_test:{3}'.format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))

clf = RandomForestClassifier()
print('Cross Validation Score: {0}'.format(np.mean(cross_val_score(clf, X_train, y_train, cv=10))))


# In[4]:


clf.fit(X_train, y_train)




pred = clf.predict(X_test)
print('Accuracy: {}'.format(accuracy_score(y_test, pred)))


# In[7]:

def decisiontree_to_json(tree):
    tree_ = tree.tree_
    feature_names = range(30)
    '''print(tree_feature)'''
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print(feature_names)
    def recurse(node):
        tree_json = dict()
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            tree_json['type'] = 'split'
            threshold = tree_.threshold[node]
            tree_json['threshold'] = "{} <= {}".format(feature_name[node], threshold)
            tree_json['left'] = recurse(tree_.children_left[node])
            tree_json['right'] = recurse(tree_.children_right[node])
        else:
            tree_json['type'] = 'leaf'
            tree_json['value'] = tree_.value[node].tolist()
        return tree_json

    return recurse(0)


def forest_to_json(forest):
    forest_json = dict()
    forest_json['n_features'] = forest.n_features_
    forest_json['n_classes'] = forest.n_classes_
    forest_json['classes'] = forest.classes_.tolist()
    forest_json['n_outputs'] = forest.n_outputs_
    forest_json['n_estimators'] = forest.n_estimators
    forest_json['estimators'] = [decisiontree_to_json(estimator) for estimator in forest.estimators_]
    return forest_json

#print(forest_to_json(clf))
json.dump(forest_to_json(clf), open('classifier.json', 'w'))


