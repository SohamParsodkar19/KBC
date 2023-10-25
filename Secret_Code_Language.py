#Write a python program to transate a message into secret code language. Use the rules below to translate nor mal English into secret code language

#Coding:
#If the word contains atleast 3 characters, remove the first letter and append it at the end ,
# now append three random characters at the starting and thee end

#else:
#   simply reverse the string

#Deconding:
#if the word contains less than 3 characters, reverse it
#else:
#   if the word has more than or equal to 3 characters, remove the last character and add it at the beginning of the string.remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

import random
import string

word = input("Enter the word : ")
# print(word)

if(len(word) > 3):
    word = word[1:] + word[0]
    random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    word = f"{random_chars}{word}{random_chars}"
    print(word)
else:
    print(word[::-1])    
    