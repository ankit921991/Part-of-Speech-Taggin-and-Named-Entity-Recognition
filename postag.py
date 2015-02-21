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

totalCount = 0
mismactCount = 0
#Extra code which wont be a part of final code
fout = open("/home/ankit/Desktop/csci544-hw2/pos.out","w")
f = open("/home/ankit/Desktop/csci544-hw2/dev.pos","r")
elines = f.readlines()
f.close()
for eline in elines:
    eline = re.sub("\n+","",eline)
    ewords = eline.split(" ")
    inputString = ""
    for eword in ewords:
        eword = eword.split("/")
        inputString = inputString + eword[0] + " " 
#Extra code end


    #for line in lines:
    line = inputString
    line = line
    line = re.sub("\n+","",line)
    line = re.sub("\s+"," ",line)
    line = re.sub("\s$","",line)
    
    words = line.split(" ")
    i=0
    pstring = ""
    while i < len(words):
        prev = "p:"
        next = "n:"
        finalWords = ""
        finalWord = ""
        finalClass = ""
        if i==0 and len(words) != 1:
            prevWord = prev    
            current = words[i]
            nextWord = words[i+1]
            nextWord = next + nextWord
            #finalWords = prevWord + " " + current +" " +  nextWord
            finalWords = prevWord + " " + current +" " +  nextWord
            i +=1
        elif i == (len(words)-1) and len(words) != 1:
            prevWord = words[i-1]
            prevWord = prev + prevWord
            current = words[i]
            nextWord = next
            #finalWords = prevWord + " " + current + " " + nextWord
            finalWords = prevWord + " " + current + " " + nextWord
            i +=1
        elif len(words) != 1 :
            prevWord = words[i-1]
            prevWord = prev + prevWord
            current = words[i]
            nextWord = words[i+1]
            nextWord = next + nextWord
            #finalWords = prevWord + " " + current + " " + nextWord
            finalWords = prevWord + " " + current + " " + nextWord
            i +=1    
        else:
            current = words[i]
            #finalWords  = prev +" " + current +" " + next
            finalWords  = prev +" " + current +" " + next
            i +=1
            
        maxClassName = classes[0]
        maxClassValue = 0
        weightCount = 0    
        finalString = ""
        finalString = finalWords    
        for _class in classes:
            weightCount = 0
            finalWords = finalString.split(" ")
            for finalWord in finalWords:
                if finalWord in weightVectors[_class]:
                        weightCount = weightCount + weightVectors[_class][finalWord]
            if weightCount > maxClassValue:
                maxClassValue = weightCount
                maxClassName = _class
        pstring = pstring + current+"/"+maxClassName + " "
    pstring = pstring + "\n"
    #print(eline + "\n" + pstring)
    #sys.stdout.flush()
    fout.write(eline + "\n" + pstring)
fout.close()
sys.exit()
        
