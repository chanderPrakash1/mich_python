#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A palindrome is a phrase that, 
if reversed, would read the exact same. 
Write code that checks if p_phrase is a 
palindrome by reversing it and then 
checking if the reversed version is equal 
to the original. Assign the reversed version 
of p_phrase to the variable r_phrase so 
that we can check your work.
"""

p_phrase = "was it a car or a cat I saw"

def reverse(s):
    str = "" 
    for i in s: 
        str = i + str
    return str
r_phrase=reverse(p_phrase)

def isPalindrome(s,r):
    if s==r:
        return True
    else:
        return False
isPalindrome(p_phrase,r_phrase)