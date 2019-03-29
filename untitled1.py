#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:14:06 2019

@author: rahul
"""

line='26,7823.2874,249.2784'
lst=[]


for char in line:
   lst.append(char)
print(lst)
for i in lst:
    if lst[i]=='.':
        lst[i]=','
    elif lst[i]==',':
        lst[i]='.'
print(lst)