#!/usr/bin/env python
# coding: utf-8

# # function to find whether a number prime or composite.
# #ASSIGNMENT SUBMITTED BY: ASHUTOSH BISHT (ROLL NO: 2022006 )

# In[1]:


def check_number(number):
    i=2
    flag=3
    while((int(number)%i!=0)&(i<=flag)): # flAG VARIABLE IS USED TO REDUCE COMPLEXITY OF THE CODE.
         flag=int(number)//i 
         i+=1
         if(i>flag):
                return True
    else:
        return False
print("enter a number")
number=int()
number=input()
type(number)
print(number)
y=check_number(number)
if(y==True):
    print(number,"is a prime number")
elif(y==False):
    print(number,"is a composite number")
            


# # For a given list generating three list of even, odd , and prime list

# In[2]:


mylist=int()
mylist=[]
even_list=[]
odd_list=[]
prime_list=[]
type(mylist)
print("how many elements you want to add in a list")
n=int()
n=input()
#type(n)
#type(mylist)
y=[0]*int(n)    # creating an array to store list elements
print("enter numbers one by one")
for i in range(int(n)):
    #mylist[i]=int()
    x=input()
    mylist.append(x)
    i+=1
print(mylist)
#conversion of list's elements to integers
for i in range(int(n)):
    y[i]=int(mylist[i])
    i+=1
#classifying nubers in 3 category i.e. even,odd and prime numbers
for i in range(int(n)):
    if(y[i]%2==0):
        even_list.append(y[i])
    elif(y[i]%2!=0):
        odd_list.append(y[i])
        z=check_number(y[i])
        if(z==True):
            prime_list.append(y[i])

print("list of even elements",even_list)
print("list of odd elements",odd_list)
print("list of prime element",prime_list)


# ### 

# In[ ]:




