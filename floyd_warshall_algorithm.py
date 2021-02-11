#!/usr/bin/env python
# coding: utf-8

# # floyds-warshell algorithm

# In[17]:


## this is the program for finding shortest distance b/w the nodes using floyds-warshell algorithm.
INFINITY=9999
v=6


# In[18]:


d = [[0, 8, 15, 10, INFINITY, INFINITY],
         [8, 0, 12, 7, 16, INFINITY],
         [15, 12, 0, INFINITY, 9, 11],
         [10, 7, INFINITY, 0, 11, 17],
         [INFINITY, 16, 9, 11, 0, 13],
         [INFINITY, INFINITY, 11, 17, 13, 0]]


# In[23]:


def fwalgorithm():
    for k in range(v):
        for i in range(v):
            for j in range(v):
                c=d[i][k]+d[k][j]
                if(d[i][j]>c):
                    d[i][j]=c
                else:
                    d[i][j]=d[i][j]

fwalgorithm()
print(d)


# In[ ]:




