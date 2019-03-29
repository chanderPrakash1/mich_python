#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write code that uses the string stored in sent
 and creates an acronym which is assigned to the
 variable acro. The first two letters of each 
 word should be used, each letter in the acronym 
 should be a capital letter, and each element of 
 the acronym should be separated by a “. ” (dot and space). 
 Words that should not be included in the acronym are stored 
 in the list stopwords. For example, if sent was assigned the 
 string “height and ewok wonder” then the resulting acronym 
 should be “HE. EW. WO”.
"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

new_lst=[]
wrd_lst=sent.split()
print(wrd_lst)
for wrd in wrd_lst:
    if wrd in stopwords:
        continue
    new_lst.append(wrd[:2].upper())
    
print(new_lst)
acro='. '.join(new_lst)
print(acro)