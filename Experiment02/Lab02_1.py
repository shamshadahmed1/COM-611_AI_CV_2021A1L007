#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""For a given set of training data examples stored in a .csv file, implement and
demostrate the data visualization to output a description of the set of all hypothesis
consistent with the training examples.
candidate elimination algorithm:"""
import numpy as np
import pandas as pd

data=pd.DataFrame(data=pd.read_csv("C:/Users/HP/Desktop/python.py/A1R006_02_1.csv"))
print(data)
concepts=np.array(data.iloc[:,0:-1])
print(concepts)

target=np.array(data.iloc[:,-1])
print(target)

def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("\n Initializiation of specific h and general h")
    print(specific_h)

    general_h=[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)

    for i,h in enumerate(concepts):
        if target[i]=="Yes":
            for x in range(len(specific_h)):

                if h[x]!=specific_h[x]:
                    specific_h[x]="?"
                    general_h[x][x]="?"

        if target[i]=="no":
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]="?"
        print("\n Steps of Candidate elimination Algorithm",i+1)
        print(specific_h)
        print(general_h)

    indices=[i for i,val in enumerate(general_h) if val==['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
s_final, g_final=learn(concepts,target)
print("\nFinal specific_h:",s_final,sep="\n")
print("\nFinal general_h:",g_final,sep="\n")


# In[ ]:





# In[ ]:




