#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:03:46 2019

@author: rahul
"""

import requests
import json

###Getting SIMILAR movies using Tastedive API
def get_movies_from_tastedive(s):
    base='https://tastedive.com/api/similar'
    para={'q':s,'type':'movies','limit':'5','k':'333966-practice-4ZAF11Y9'}
    resp=requests.get(base,params=para)
    #print(resp.url)
    #print(resp.text)
    return resp.json()

#####Extracting Movie Title from The data of tastedive api
def extract_movie_titles(d):
    movie_titles=[]
    for itm in d['Similar']['Results']:
        movie_titles.append( itm['Name'])
    return(movie_titles)

######### Getting movie related to each Title
def get_related_titles(lst):
    lst2=[]
    for movie in lst:
        movie_d=get_movies_from_tastedive(movie)
        movie_title=extract_movie_titles(movie_d)
        for mvi in movie_title:
            if mvi not in lst2:
                lst2.append(mvi)
            
    return lst2


######### Getting DAta of movie for each Title Using OMDB API
def get_movie_data(s):
    base='http://www.omdbapi.com/'
    param={'t':s,'r':'json','apikey':'d9c2ce53'}
    rsp=requests.get(base,params=param)
    return rsp.json()

# Getting Rotten Tomatoes Rating From OMDB API
def get_movie_rating(d):
    print(d)
    lst_rating=d['Ratings']
    #print(lst_rating)
    for rating in lst_rating:
        for key in rating.keys():
            if rating[key]=='Rotten Tomatoes':
                #print('yes')
                rated=rating['Value']
                if len(rated)==2:
                    return(rated[:1])
                else:
                    return(int(rated[:2]))
            
    return 0

def get_rating_list(lst):
    ratings=[]
    for title in lst:
        movie_data=get_movie_data(title)
        movie_rating=get_movie_rating(movie_data)
        ratings.append(movie_rating)
    return ratings

movie_name=input('Enter Movie Name: ')
movie_from_tastedive=get_movies_from_tastedive(movie_name)
movie_titles=extract_movie_titles(movie_from_tastedive)
related_titles=get_related_titles(movie_titles)
rating_list=get_rating_list(related_titles)
for title,rating in zip(related_titles,rating_list):
    print('Movie: {} , Rotten Tomatoes Rating: {}'.format(title,rating))
    



    

