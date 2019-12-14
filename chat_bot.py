# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:03:28 2019

@author: lenovo-pc
"""

#building a chatbot with deep nlp
import numpy as np
import time
import re
import tensorflow as tf



################# PART-1 DATA PREPROCESSING ###############

# Loading the dataset 

lines=open("movie_lines.txt",encoding='utf-8', errors='ignore').read().split('\n')
conversations=open("movie_conversations.txt",encoding='utf-8', errors='ignore').read().split('\n')

# Creating Dictionary

id2line={}

for line in lines:
    _line=line.split(" +++$+++ ")
    if len(_line)==5:
        id2line[_line[0]]=_line[4]
 
# Creating list of conversation ids

conversation_ids=[]
for conversation in conversations[:-1]:
    _conversation=conversation.split(" +++$+++ ")[-1][1:-1].replace("'","").replace(" ","")
    conversation_ids.append(_conversation.split(","))
    
# Getting separately the questions and answers

questions=[]
answers=[]

for conversation in conversation_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        
        
# Doing a first cleaning of the text

def clean_text(text):
    text=text.lower()
    text = re.sub(r"i'm","i am",text)        
    text = re.sub(r"he's","he is",text)        
    text = re.sub(r"she's","she is",text)        
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"\'ll","will",text)
    text = re.sub(r"\'ve","have",text)
    text = re.sub(r"\'re","are",text)
    text = re.sub(r"\'d","would",text)
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"we'd","we would",text)
    #text = re.sub(r"[-()[]\"#@:;<>{}+=!%^&*_.?,]","",text)
    text = re.sub(r"[.?,@#$%^&*()]","",text)
    
    return text
    
# Cleaning questions and answers

clean_questions=[]
for question in questions:
    clean_questions.append(clean_text(question))    

clean_answers=[]
for answer in answers:
    clean_answers.append(clean_text(answer))    

    
# Creating a dictionary that maps the word to its number of occurances
word2count={}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word]=1
        else:
            word2count[word] += 1
                
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word]=1
        else:
            word2count[word] += 1
                
        






        