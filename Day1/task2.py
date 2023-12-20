# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:11:20 2023

@author: joepo
"""
from collections import OrderedDict

word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert_first_last_numbers(line):
    first_indices={}
    last_indices={}
    for word in word_to_digit.keys():
        last=line.rfind(word)
        first=line.find(word)
        first_indices[word]=first
        last_indices[word]=last
        
    fi = {k: v for k, v in first_indices.items() if v > -1}
    li = {k: v for k, v in last_indices.items() if v > -1}
    FI = OrderedDict(sorted(fi.items(), key=lambda t: t[1]))
    LI = OrderedDict(sorted(li.items(), key=lambda t: t[1]))
    if len(FI)==0 and len(LI)==0:
        return line
    first_word=list(FI.keys())[0]
    first_index=FI[first_word]
    last_word,last_index=list(LI.items())[-1]
    
    line=line[:first_index]+word_to_digit[first_word]+line[first_index+len(first_word):]
    if first_index ==last_index:
        return line
    overlap  = (first_index + len(first_word)) - last_index
    if overlap < 0:
        overlap =0
    last_index = last_index - len(first_word)+1 + overlap
    line=line[:last_index]+word_to_digit[last_word]+line[last_index+len(last_word):]
    print(line)
    return line

f = open("input.txt", "r")
lines = f.readlines()
count=0
for line in lines:
    line=convert_first_last_numbers(line)
    numbers=filter(lambda n: n.isnumeric(),line)
    numbers=list(numbers)
    x = numbers[0]
    y = numbers[-1]
    z=x+y
    count=count+int(z)
    
print(count)