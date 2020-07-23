#!/usr/bin/env python
# coding: utf-8

# In[35]:


print("program to check whether number is prime or not")
num=int(input("enter the number:\n"))
temp=num
if num>1:
    for x in range(2,num):
        if(num%x)==0:
            var=num//x
            print(f"the number is not a prime number\n")
            break
        else: 
            print("number is a prime number")
else:
    print("number is not a prime number")

