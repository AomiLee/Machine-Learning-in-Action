#!/usr/bin/env python
# coding: utf-8

# # KNN: k Nearest Neighbors
# Input:      
# inX: vector to compare to existing dataset (1xN)  
# inX:测试集
# 
# dataSet: size m data set of known vectors (NxM)  
# dataSe：训练集
# 
# labels: data set labels (1xM vector)  
# labels：数据已知分类
# 
# k: number of neighbors to use for comparison (should be an odd number)  
# 
# Output:       
# the most popular class label
# Output：数量最多的分类
# 
# inX是你要输入的要分类的“坐标”，dataSet是上面createDataSet的array，就是已经有的，分类过的坐标，label是相应分类的标签，k是KNN，k近邻里面的k

# In[ ]:


import numpy as np
import operator
from os import listdir


# In[ ]:


#定义分类器
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0] #dataSetSize是sataSet的行数
    diffMat = np.tile(inX,(dataSetSize,1))-dataSet#(x11-x12)，(x21-x22)
    #tile是用来复制数组的函数，用来复制inX，reps如果是（n,1）表示把整个数组复制n次,reps如果是数字n，表示数组的每个元素复制n次
    sqDiffMat = diffMat**2#(xi1-xi2)^2
    sqDistances = sqDiffMat.sum(axis=1)#axis=1是列相加，，这样得到了(x1-x2)^2+(x21-x22)^2
    distances = sqDistances**0.5
    sortedDisIndicies = distances.argsort()#argsort是排序，将元素按照由小到大的顺序返回下标，比如([3,1,2]),它返回的就是([1,2,0])
    
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        #得到sortedDisIndicies里第i个元素的标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #get是取字典里的元素，如果之前这个voteIlabel是有的，那么就返回字典里这个voteIlabel里的值，如果没有就返回0（后面的参数），
        #这行代码的意思就是算离目标点距离最近的k个点的类别，这个点是哪个类别哪个类别就加1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    #classCount.items()表示将classCount字典分解为元祖列表
    #key=operator.itemgetter(1)的意思是按照字典里的第一个排序，{A:1,B:2},要按照第1个（AB是第0个），即‘1’‘2’排序。
    #reverse=True是降序排序
    return sortedClassCount[0][0]#返回类别最多的类别    
    


# # API
# 
# numpy.tile(A, reps) 
# 功能:将矩阵A看成一个整体， 按照reps的方式复制 
# 参数:A：输入矩阵; reps:每个坐标重复的次数 
# 返回值:输出矩阵
# 
# array.shape[0]表示查看数组的行数  
# array.shape[1]表示查看数组的列数
# 
# operator模块  
# 参考https://blog.csdn.net/shengmingqijiquan/article/details/53005129
# 
# key=operator.itemgetter(k)  
# 参考http://www.cnblogs.com/zhoufankui/p/6274172.html
# 

# In[ ]:




