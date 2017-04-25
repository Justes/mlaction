# -*- coding:utf-8 -*-
from math import log

def createDataSet():
    dataSet = [
            [1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']
            ]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries # 计算每个类别的概率
        shannonEnt -= prob * log(prob,2) # 以2为底求对数
    return shannonEnt
