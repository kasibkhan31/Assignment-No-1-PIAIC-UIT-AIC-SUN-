#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Kasib Khan"
print(a)


# In[2]:


fav_quote = 'Im not in danger im the danger.'
print("Walter White once said,",'"',fav_quote,'"')


# In[3]:


# area = pi x rxr
radius = float(input('Enter the radius: '))
pi = 3.142
area = pi * radius**2
print('Area of Circle with', radius, 'is', area)


# In[4]:


num = float(input("Enter the Number: "))
if num > 0:
    print("Positive Number Entered")
elif num < 0:
    print("Negative Number Entered")
else: 
    print('Zero Entered')


# In[5]:


char = input('Enter a Character: ')
if char in ("a","e","i","o","u","A","E","I","O","U"):
    print('Letter',char, 'is', 'Vowel')
else:
    print('Letter',char, 'is', 'Not Vowel')


# In[6]:


weight = float(input("Enter your Weight in KG: "))
height = float(input("Enter your Height in ft: "))

cm_height = height * 30.48      #Convert height ft into cm
print(f"Height in cm:{cm_height: .2f}")

height_m = cm_height / 100     #convert height cm into meter
print(f"Height in Meter:{height_m: .2f}")

print('---------------------------------')

bmi = weight / (height_m * height_m)  #BMI formulaa weight / height in Sq.meter 
print(f"Your BMI is: {bmi:.2f}")
print('---------------------------------')


# In[7]:


names = ["Alii", "Hussain", "Haider","Abbass"]
for i in names:
    print(i)


# In[8]:


names = ["Alii", "Hussain", "Haider","Abbsss"]
for i in names:
    print(f" Hello {i}, How Are you? ")


# In[12]:


foods = ["Biryani", "Seekh Kabab", "Pulao", "Malai Boti", "Chapli Kabab", "Korma", "Tandoori Chicken", "Broast", "Reshmi Kabab"]
print("The First 03 Items in the List are:", foods[0:3])
print("The Middle 03 Items in the List are:", foods[3:6])
print("The Last 03 Items in the List are:", foods[6:])


# In[19]:


foods = ["Biryani", "Seekh Kabab", "Pulao", "Malai Boti", "Chapli Kabab", "Korma", "Tandoori Chicken", "Broast", "Reshmi Kabab"]
friends_foods = foods[::-1]   #Reversing the original List to make a new list
print(friends_foods)
foods.append("Pizza")      #append the New Item in the original food List
friends_foods.append("Gobi")  #append the New Item in the friends foods list
print(foods)
print(friends_foods)
if foods == friends_foods:
    print("Both List are Same")
else:
    print("Both List are Different")
    print("My Favorite Foods are: ")
for myfav in foods:
    print(myfav)
    print("My Friends Favorite Foods: ")
for myfriends in friends_foods:
    print(myfriends)


# In[ ]:





# In[ ]:




