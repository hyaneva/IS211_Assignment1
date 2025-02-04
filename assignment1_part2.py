#!/usr/bin/env python
# coding: utf-8

# In[4]:


#2

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}.")


# In[8]:


#3

book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")


# In[9]:


#4

book1.display()  # Output: Harry Potter and the Goblet of Fire, written by J. K. Rowling
book2.display()  # Output: Ivanhoe: A Romance, written by Walter Scott


# In[ ]:




