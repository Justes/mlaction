# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

# boxstyle 为文本框类型,sawtooth是锯齿形,fc是边框粗细
decisionNode = dict(boxstyle="sawtooth",fc="0.8")
# 定义叶子结点的属性
leafNode = dict(boxstyle="round4",fc="0.8")
# 定义箭头属性
arrow_args = dict(arrowstyle="<-")

# 在父子节点间填充文本信息
def plotMidText(cntrPt,parentPt,txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree(myTree,parentPt,nodeTxt):
    # 计算宽高
    numLeafs = getNumLeafs(myTree) 
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    # 根据子节点的个数确定当前节点的位置
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW,plotTree.yOff) 
    # 标记子节点属性值
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    # 减少y偏移
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


# 绘制结点
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    # annotate 是关于一个数据点的文本 
    # nodeTxt 是要显示的文本 xy 被注释的地方, xytext 插入注释内容的地方
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)

# 创建绘图
def createPlot(inTree):
    # 定义画布,背景白色
    fig = plt.figure(1,facecolor='white')
    # 清空画布
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    # createPlot.ax1 为全局变量,绘制图像的句柄,subplot 为定义了一个绘图,111表示figure中的图有1行1列即1个,最后的1表示第一个图
    # frameon 表示是否绘制坐标轴矩形
    createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree,(0.5,1.0),'')
    plt.show()

# 获取叶子节点的数目
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

# 获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else :
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},{'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0:'no',1:'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]
