# -*- coding:utf-8 -*-
from numpy import *

def loadDataSet():
    postingList = [['my','dog','has','flea','problems','help','please'],
            ['maybe','not','take','him','to','dog','park','stupid'],
            ['my','dalmation','is','so','cute','I','love','him'],
            ['stop','posting','stupid','worthless','garbage'],
            ['my','licks','ate','my','steak','how','to','stop','him'],
            ['quit','buying','worthless','dog','food','stupid']
            ]
    classVec = [0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([]) # 创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document) # 创建两个集合的并集
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0] * len(vocabList) # 创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWords) # 初始化概率
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] # 向量相加
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i]) 
    p1Vect = p1Num / p1Denom # 对每个元素做除法
    p0Vect = p0Num / p0Denom
    return p0Vect,p1Vect,pAbusive