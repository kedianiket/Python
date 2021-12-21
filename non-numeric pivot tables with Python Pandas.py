#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime

import matplotlib.pyplot as plt

import seaborn as sns


# In[2]:


#changing working directory
get_ipython().run_line_magic('cd', '"E:\\Python\\Pivot Table"')


# In[3]:


empData = pd.read_csv('mdl_feedback_dated.csv')


# In[4]:


empData['Key1'] = empData['course']+"-"+empData['user_id'].astype(str)


# In[5]:


empData['Key2'] = empData['feedback']+"-"+empData['question']


# In[14]:


pivot_table = empData.pivot_table(index='Key1',
                                     columns='Key2', 
                                     values='answer_text',
                                     aggfunc=lambda x: '###'.join(str(v) for v in x))


# In[16]:


pivot_table.to_csv('outputtttt.csv')


# In[ ]:




