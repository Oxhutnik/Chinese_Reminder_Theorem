#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np


# In[39]:


# a function for calculating whether given numbers are relative prime
def is_rlt_prime(a,b):
    a = int(a)
    b = int(b)
    arr1 = np.array([])
    arr2 = np.array([])
    arr3 = np.array([])
    #To calculate the divisors of numbers
    for i in range(2,a+1):
        if a % i == 0:
            arr1 = np.append(arr1,i)
    for i in range(2,b+1):
        if b % i == 0:
            arr2 = np.append(arr2,i)
    #if there are any same value except 1 than function will return false
    arr3 = np.intersect1d(arr1,arr2)
    if len(arr3) == 0:
        print("given numbers are relative prime.")
        return a,b
    else :
        print("given numbers are not realtive prime. The procede is gonna stop")
        return False




# In[40]:


def func1(a,b,a1,b1):
    if is_rlt_prime(a,b) == False:
        return False
    if a1>a or b1>b:
        print("first values are higher than modes. pls fix that")
        inp = input("if you want i can fix .yes or no  ")
        if inp == "no":
            return
        if inp == "yes":
            if a1>a:
                a1 = a1-a
                if b1>b:
                    b1 = b1-b 
            else:
                b1 = b1-b
    c = int(a*b)
    d = 0
    e = 0
    arr1=np.array([])
    arr2=np.array([])    
    #We make a list of the modes and the sum of the numbers
    for i in range(c):
        d = a*i + a1
        e = b*i + b1
        arr1 = np.append(arr1,d)
        arr2 = np.append(arr2,e)
    #and we look for a same value
    arr3 = np.intersect1d(arr1, arr2)
    a = arr3[1]-arr3[0]
    a1 = arr3[0]
    if a1>a:
        a = a1-a
    #return the same value and mod
    return a,a1
        


# In[41]:


def func2(a,b):
    #we define our first values, mod and base number
    aa = a[0]
    aa1 = b[0]
    for i in range(len(a)-1):
        #then we keep repeating it until all numbers are calculated
        aa,aa1 = func1(aa,a[i+1],aa1,b[i+1])
    return aa,aa1





