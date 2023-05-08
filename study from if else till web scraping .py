#!/usr/bin/env python
# coding: utf-8

# # if and else

# write a program to accept the no from 1 to 7 and disp the name like 1 for sunday

# In[1]:


num=int(input('enter the number between 1 and 7:'))
if num==1:
    print('its sunday')
elif num==2:
    print('its monday')
elif num==3:
    print('its tuesday')
elif num==4:
    print('its web')
elif num==5:
    print('its thu')
elif num==6:
    print('its fri')
elif num==7:
    print('its sat')
else:
    print('enter any no between 1-7')


# wrute a pro to wether no is accepted from user is divi by 2 n 3 both

# In[3]:


num=int(input('enter the no'))
if num%2==0 and num%3==0:
    print('num is devi by 2 n 3')
else:
    print('no is not devi by 2 n 3')


# accept the temp in degree celsius of water n check wether its bolilng or not

# In[4]:


temp=int(input('nter thr temp'))
if temp>=100:
    print('its boiling')
else:
    print('its cold ')


# In[2]:


num=int(input('enter the age'))
if num%5==0:
    print('hello')
else:
    print('bye')


# In[5]:


amt=0
num-int(input('enter the unit of bill'))
if num<=100:
        amt=0
if num>100 and num<=200:
        amt=(num-100)*5
if num>200:
        amt=(num-200)*10
if num>350:        
print('ur bill is due')
        


# write a pro to check wether tha last digit of a num(enter by user)  is diviv by 3 or not

# In[7]:


num=int(input('enter any num'))
id=num%10
if id%3==0:
    print('last dig of num div by 3')
else:
    print('not divisible')
    


# wap to acept the cost price of bike n disp the road tax to be paid acc the foll crit

# In[9]:


tax=0
per=int(input('enter the price of bike'))
if per>100000:
    tax=15/100*per
elif per>50000 and per<=100000:
    tax=10/100*per
else:
    tax=5/100*per
print('tax to be paid',tax)


# write a program to check whether an years is leap year or not.

# In[11]:


yr=int(input('enter the year'))
if yr%100==0:
    if yr%400==0:
        print('enter yr is leap yr')
else:
    if yr%4==0:
        print('is leap yr')
    else:
        print('is not')


# In[ ]:





# In[ ]:





# # nasteb loop

# In[12]:


num=int(input('enter the no'))

if (num>=0):
    if (num==0):
        print('the no is zero')
    else :
        print('post')
else:
    print('neg')        
        

        


# Question..The program below is an example of that. We first check if the person is an adult. Then we make additional comparisons to see if he or she graduated or gotten a drivers license:

# In[13]:


age = 19
isGraduated = False
hasLicense = True

# Look if person is 18 years or older
if age >= 18:
    print("You're 18 or older. Welcome to adulthood!")

    if isGraduated:
        print('Congratulations with your graduation!')
    if hasLicense:
        print('Happy driving!')



# In[13]:


var=100
if var<200:
    print('exp value is less then 200')
    if var==150:
        print('its 150')
    elif var==100:
        print('its 100')
    elif var==50:
        print('its 50') 
    elif var==50:
        print('exp value is greater then50') 
else:
    print('could not be true')
    print('good bye')
        


# In[ ]:




