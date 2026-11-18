#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


numbers = list(range(1000))
print(numbers[:10])


# In[ ]:


get_ipython().run_line_magic('timeit', '[x*x for x in numbers]')


# In[ ]:





# In[ ]:




