#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import operator
# import KNN_filematrix as KNN


# In[7]:


# dataData,dataLabels = KNN.filematrix('datingTestSet2.txt')


# In[8]:


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals,(m,1))#把minVals复制m次，和dataSet里面对应元素相减
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minVals


# In[9]:


# normDataSet,ranges,minVals = autoNorm(dataData)
# print(normDataSet)


# In[10]:


# print(ranges)


# # In[11]:


# print(minVals)

