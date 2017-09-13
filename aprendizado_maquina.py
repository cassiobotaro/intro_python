#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn import tree

# 1 suave, 0 irregular
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# 0 maçã, 1 laranja
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))
