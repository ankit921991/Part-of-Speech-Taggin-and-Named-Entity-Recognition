import re
import math
import os
import sys
from sys import stdin


inputPath = sys.argv[1]  #input file path from command line
#outputPath = sys.argv[2] #out file path command line

print("Enter the sentense ")
inputString = stdin.readline()

f = open(inputPath,"r")
lines = f.readlines()
f.close()

# to retrieve the classes
line = ''
line = lines[0];
i = 1
classes = []
weightVectors = {}
words = line.split(' ')
rowLength = len(words)
while i < rowLength:
    classes.append(words[i])
    weightVectors[words[i]] = {} # initialize dictionary for weight vectors
    i +=2
'''for _class in classes:
    print(_class)'''
#---------------------------

# populate dictionaries for wightVector
for line in lines:
    words = line.split(" ")
    i=1    
    while i < rowLength:
        weightVectors[words[i]][words[0]] = float(words[i+1])
        i = i + 2    
#----------------------

'''f = open(outputPath,"r")
lines = f.readlines()
f.close()'''

#for line in lines:
line = inputString
words = line.split(" ")
i=0
while i < len(words):
    prev = "p:"
    next = "n:"
    finalWord = ""
    finalClass = ""
    if i==0 and len(words) != 1:
        prevWord = prev    
        current = words[i]
        #current = words[i].split("/")
        nextWord = words[i+1]
        #nextWord = words[i+1].split("/")
        nextWord = next + nextWord
        finalWord = prevWord + current + nextWord
        #finalClass = current[1]
        #finalClass = finalClass + " " + finalWord + "\n"
        i +=1
    elif i == (len(words)-1) and len(words) != 1:
        prevWord = words[i-1]
        prevWord = prev + prevWord
        current = words[i]
        nextWord = next
        finalWord = prevWord + current + nextWord
        i +=1
    elif len(words) != 1 :
        prevWord = words[i-1]
        prevWord = prev + prevWord
        current = words[i]
        nextWord = words[i+1]
        nextWord = next + nextWord
        finalWord = prevWord + current + nextWord
        i +=1    
    else:
        current = words[i]
        finalWord  = prev+current+next
        i +=1
        
    maxClassName = classes[0]
    maxClassValue = 0
    weightCount = 0    
    for _class in classes:
        weightCount = 0
        if finalWord in weightVectors[_class]:
                weightCount = weightCount + weightVectors[_class][finalWord]
        if weightCount > maxClassValue:
            maxClassValue = weightCount
            maxClassName = _class
    print(current+"/"+maxClassName)
                
        
