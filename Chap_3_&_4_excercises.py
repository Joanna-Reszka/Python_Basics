#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 3.2.1 Syntax Error
print("Hello World)


# In[5]:


# 3.2.2 Name Error
print(Hello, World)


# In[6]:


# 3.3.1
print("Display text")


# In[7]:


# 3.3.2 
greeting = 'Hi there'
print(greeting)


# In[8]:


# 4.1.1
print('She said:"Hurry up!"')


# In[9]:


# 4.1.2
print("Hell's Kitchen has delicious food")


# In[20]:


# 4.1.3
text =('''A black hole is a place in space where gravity pulls so much
      that even light can not get out. The gravity is so strong because
      matter has been squeezed into a tiny space. ''')
print(text)


# In[21]:


# 4.1.4
text = ("A black hole is a place\
 in space where gravity pulls so much\
 that even light can not get out.")
print(text)


# In[23]:


# 4.2.1
text = "Hell's Kitchen has delicious food"
print(len(text))


# In[25]:


# 4.2.2
word1 = 'Kogiel'
word2 = 'Mogiel'
joined = word1 + word2
print(joined)


# In[24]:


# 4.2.3
name = 'Sherlock'
surname = 'Holmes'
fullname = name + ' ' + surname
print(fullname)


# In[26]:


# 4.2.4
word = 'bazinga'
print(word[2:6])


# In[28]:


# 4.3.1
strings = ["Animals","Badger", "Honey Bee", "Honeybadger"]
for word in strings:
    print(word.lower())


# In[29]:


# 4.3.2
strings = ['animals', 'badger', 'honey bee', 'honeybadger']
for word in strings:
    print(word.upper())


# In[33]:


# 4.3.3
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())


# In[34]:


# 4.3.4
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print(string1.startswith('be'))
print(string2.startswith('be'))
print(string3.startswith('be'))
print(string4.startswith('be'))


# In[41]:


# 4.3.5
string1 = "Becomes"
mod1a = "b" + string1[1:]
mod1b = string1.lower()
print(mod1a.startswith('be'))
print(mod1b.startswith('be'))
string3 = "BEAR"
print(string3.lower().startswith('be'))
string4 = " bEautiful"
print(string4.lstrip().lower().startswith('be'))


# In[1]:


# 4.4.1
name =input("Type your name: ")
print(name)


# In[2]:


# 4.4.2
name =input("Type your name: ")
print(name.lower())


# In[4]:


# 4.4.3
name =input("Type your name: ")
print(len(name))


# In[6]:


# 4.5.1 first_letter
password = input("Enter your password: ")
print(f"The first letter you entered was : {password[0].upper()}")


# In[8]:


# 4.6.1
age = int(input("Enter your age: "))
print(f"That was your half aged you: {age*0.5}")


# In[11]:


# 4.6.2
weight = float(input("Enter your weight: "))
print(f"That is quarter of your weight: {weight*0.25}")


# In[12]:


# 4.6.3
measure = "temperature"
value = 3.5
print(f"{measure.title()} is {str(value)} degrees Celcius")


# In[16]:


# 4.6.4
nr1 = float(input("Enter first number: "))
nr2 = float(input("Enter second number: "))
print(f"The product of {nr1} and {nr2} is {nr1*nr2}")


# In[17]:


# 4.7.1
weight = 0.2
animal = 'newt'
print(str(weight) + " kg is the weight of the " + animal)


# In[22]:


# 4.7.2
weight = 0.2
animal = 'newt'
print("{} kg is the weight of the {}".format(str(weight),animal))


# In[23]:


# 4.7.3
weight = 0.2
animal = 'newt'
print(f"{str(weight)} kg is the weight of the {animal}")


# In[24]:


# 4.8.1
'AAA'.find('a')


# In[25]:


# 4.8.2
"Somebody said something to Samantha.".replace('s','x')


# In[29]:


# 4.8.3
text = input("Type a word or a sentence: ")
letter = input("Type a letter: ")
print(text.find(letter.lower()))


# In[40]:


# 4.9
text = input("Enter some text: ")
letters = ['a','b','e','l','o','s','t']
numbers = [4,8,3,1,0,5,7]
coder = dict(zip(letters, numbers))
#print(coder)
for letter in text:
    if letter in coder.keys():
        text = text.replace(letter, str(coder[letter]))
print(text)
        


# In[ ]:




