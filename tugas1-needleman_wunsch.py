
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
i= 0
j= 0

A = "HNALQRR"   #as. amino 1
B = "HALQRT"    #as. amino 2
blosum = pd.read_csv("BLOSUM62.txt", delim_whitespace = True)

A = list("-")+list(A)  #declare A dengan gap di awal
B = list("-")+list(B)  #declare B dengan gap di awal
blosum


# In[2]:


#Create matriks F
F = [[0 for x in range(len(B))] for x in range(len(A))] # matriks dengan
for i in range(len(A)):
    print (F[i])
d = -4 #skor penalty jika terdapat gap


# In[3]:


#Hitung value tiap cell pada F
for i in range(0,len(A)):
    F[i][0] = d*i #set kolom dengan nilai akumulatif gap penalty 
for j in range(0,len(B)):
    F[0][j] = d*j #set baris dengan nilai akumulatif gap penalty
for i in range(1, len(A)):
    for j in range(1, len(B)):
        match = F[i-1][j-1] + blosum [A[i]][B[j]]  #hitung value
        delete = F[i-1][j] + d                     #hitung value
        insert = F[i][j-1] + d                     #hitung value
        F[i][j] = max (match,insert,delete)        #set value untuk tiap cell diliat dari nilai max
for i in range(len(B)):
    print (F[i]) 


# In[4]:


#alignment
AlignA = ''
AlignB = ''
i = len(A)-1
j = len(B)-1
while(i>0 or j>0):
    if (i>0 and j>0 and F[i][j] == F[i-1][j-1] + blosum[A[i]][B[j]]):
        AlignA = A[i] + AlignA
        AlignB = B[j] + AlignB
        i = i-1
        j = j-1
    elif (i>0 and F[i][j] == F[i-1][j] + d):
        AlignA = A[i] + AlignA
        AlignB = '-' + AlignB
        i = i-1
    elif (j>0 and F[i][j] == F[i][j-1] + d):
        AlignA = '-' + AlignA
        AlignB = B[i] + AlignB
        j = j-1
print(AlignA)
print(AlignB)

