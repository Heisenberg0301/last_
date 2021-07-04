#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys 
import factorial
try:
    var = factorial.GFG()
    #sys.exit(0)
except AttributeError:
    print("required class is not present")
    sys.exit(1)
sys.exit(0)


# In[ ]:




