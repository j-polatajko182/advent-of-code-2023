# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:44:50 2023

@author: joepo
"""

f = open("Input.txt", "r")
lines = f.readlines()
count=0
for line in lines:
    numbers=filter(lambda n: n.isnumeric(),line)
    numbers=list(numbers)
    x = numbers[0]
    y = numbers[-1]
    z=x+y
    count=count+int(z)
    
print(count)    
#numbers = open("example.txt", "r")

  #Using a lambda function
#positive_numbers = filter(lambda n: n > 0, lines)
#positive_numbers
#list(positive_numbers)


 
#def is_positive(n):
#    return n > 0
#...
#list(filter(is_positive, numbers))

#for line in lines:
 #   filter(line)
    


#x = line.isnumeric()
#if x is false:
    
    

#print(x)

