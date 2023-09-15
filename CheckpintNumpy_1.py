#!/usr/bin/env python
# coding: utf-8

# In[78]:


#1.Importer le bibliotheque Numpy
import numpy as np
#2. Importer les donnees
with open('/Users/mac/Downloads/Loan_prediction_dataset.csv', 'r') as file:
    # 2. Lire les données CSV et les stocker dans un tableau numpy
    data = np.genfromtxt(file, delimiter=',', skip_header=2)


# In[79]:


print(data)


# In[80]:


#3. calcul de la moyenne, mediane et ecart type
Loan_Amount = data[:, 8]


# In[81]:


#Calcul de la moyenne :
np.nanmean(Loan_Amount)


# In[86]:


#calcul de la mediane
np.nanmedian(Loan_Amount)


# In[87]:


#calcul de l'ecartype
np.nanstd(Loan_Amount)


# In[ ]:




