#!/usr/bin/env python
# coding: utf-8

# # 把txt文件转化为特征值矩阵加分类矩阵

# In[1]:


import numpy as np
import operator
# import pandas as pd


# In[4]:


#观察数据结构
# data = pd.read_csv('datingTestSet.txt',header = None)
# data.head(5)


# In[ ]:


def filematrix(filename):
    love_dictionary = {'largeDoses':3,'smallDoses':2,'didntLike':1}
    #定义1,2,3种分类的标签
    fr = open(filename)
    arrayLines = fr.readlines()
    #一次读取整个文本数据，并且自动将文件内容分析成一个行的列表，
    number_of_lines = len(arrayLines)#得到字符串列表的个数，也就是行数
    returnMat = np.zeros((number_of_lines,3))#准备特征矩阵
    classLabelVector = []#准备分类值返回矩阵
    index = 0
    for line in arrayLines:
        line = line.strip()#去掉首尾的空格
        listFromLine = line.split('\t')
        #矩阵中，每遇到一个'\t',便依次将这一部分赋给列表中一个元素，返回值为列表 
        returnMat[index,:] = listFromLine[0:3]
        #将每一行的前三个元素依次赋值给特征矩阵
        if(listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        #对于每一行最后一列，按照其值得不同，给分类值返回矩阵赋值,具体逻辑见test
        index += 1
        #每执行一次，便向下一行再循环
    return returnMat,classLabelVector
    #returnMat：三个特征组成的特征的矩阵
    #classLabelVector：分类矩阵 


# # API
# readlines()  
# 参考：https://www.cnblogs.com/xiugeng/p/8635862.html
# 
# strip()  
# 参考：https://www.cnblogs.com/itdyb/p/5046472.html
# 
# split()  
# 参考：https://www.cnblogs.com/huchong/p/7349886.html
# 
# get()  
# 参考：http://www.runoob.com/python3/python3-att-dictionary-get.html
# 
# isdigit()  
# 参考：http://www.runoob.com/python3/python3-string-isdigit.html

# In[ ]:




