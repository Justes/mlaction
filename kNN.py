from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def autoNorm(dataSet):
    minVals = dataSet.min(0) # 每一维最小值 
    maxVals = dataSet.max(0) # 每一维最大值
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet)) # 全0矩阵 shape获取矩阵形状 zeros补0
    m = dataSet.shape[0] # 矩阵第一维长度
    normDataSet = dataSet - tile(minVals,(m,1)) # tile 用minVals创建矩阵,维度跟minVals一样,矩阵高度为m . tile第二个参数里的m为在列上补齐m行，参数里的1,为在矩阵行上只有1次
    normDataSet = normDataSet / tile(ranges,(m,1)) # 归一化处理
    return normDataSet,ranges,minVals

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    print(classCount)
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
