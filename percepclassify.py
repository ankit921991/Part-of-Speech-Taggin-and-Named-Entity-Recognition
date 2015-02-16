import re
import math
import os
import sys

inputPath = sys.argv[1]  #input file path from command line
outputPath = sys.argv[2] #out file path command line
outfile = ""

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

f = open(outputPath,"r")
lines = f.readlines()
f.close()

for line in lines:
    words = line.split(" ")
    maxClassName = classes[0]
    maxClassValue = 0
    weightCount = 0    
    for _class in classes:
        weightCount = 0
        for word in words:
            if word in weightVectors[_class]:
                weightCount = weightCount + weightVectors[_class][word]
        if weightCount > maxClassValue:
            maxClassValue = weightCount
            maxClassName = _class
    print(maxClassName)
                
        
