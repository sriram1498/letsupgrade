#!/usr/bin/env python
# coding: utf-8

# In[2]:


list_keys = ['ram','karthi','dhanam','hepsi']
list_values = [21,20,19,17]
result = {}
for key in list_keys:
    for values in list_values:
        result[key] = values
        list_values.remove(values)
        break
print(str(result))


# In[ ]:




