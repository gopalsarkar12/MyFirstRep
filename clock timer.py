#!/usr/bin/env python
# coding: utf-8

# In[21]:


import time


# In[25]:


result= time.localtime()


# In[26]:


print(result)


# In[ ]:


while True:
    result=time.localtime()
    if result.tm_hour==16 and result.tm_min==11:
        print("Hey! Dude It's Time to Wake-up")
        break


# In[ ]:





# In[ ]:





# In[ ]:




