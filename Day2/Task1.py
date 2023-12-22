# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:52:56 2023

@author: joepo
"""

#Determine which games would have been possible if the bag has 12 red cubes, 13 green cubes, and 14 blue cubes
#identify which colours are in the line and their correspoinding numbers
#check if values exceed allowed values
#if values do not exceed add index number to a count
#if values exceed allowed values sack them off

f = open("Input.txt", "r")
lines = f.readlines()
count=0
for line in lines:
    x = line.split(":")
    y=x[1].split(";")
    valid=True
    for figure in y:
        draws=figure.split(",")
        for a in draws:
            colours=a.strip().split(" ")
            if 'blue' in colours:
                if int(colours[0])<=14:
                    pass
                else:
                    valid=False
            if 'green' in colours:
                if int(colours[0])<=13:
                    pass
                else:
                    valid=False
            if 'red' in colours:
                if int(colours[0])<=12:
                    pass
                else:
                    valid=False
    if valid==False:
        pass
    else:
        gameid=x[0].split(" ")
        count = count + int(gameid[1])
print(count)               
                    
                
        

    