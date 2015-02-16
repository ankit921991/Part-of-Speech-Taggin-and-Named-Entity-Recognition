import os
import sys
import re
import random
import subprocess

inputPath = sys.argv[1]
outputPath = sys.argv[2]

classes = []

f = open(inputPath,"r")
lines = f.readlines()
f.close()



f = open(outputPath,"w")
for line in lines:
    i=0
    line = re.sub("\n+","",line)
    line = re.sub("\s+"," ",line)
    line = re.sub("\s$","",line)
    line = re.sub("^\s","",line)
    words = line.split(" ")
    #print(str(len(words)))
    while i < len(words):
        prev = "p:"
        next = "n:"
        finalWord = ""
        finalClass = ""
        if i==0 and len(words) != 1:
            prevWord = prev    
            current = words[i]
            current = words[i].split("/")
            nextWord = words[i+1]
            nextWord = words[i+1].split("/")
            nextWord = next + nextWord[0]
            finalWord = prevWord + current[0] + nextWord
            finalClass = current[1]
            finalClass = finalClass + " " + finalWord + "\n"
            i +=1
        elif i == (len(words)-1) and len(words) != 1:
            prevWord = words[i-1]
            prevWord = words[i-1].split("/")
            prevWord = prev + prevWord[0]
            current = words[i]
            current = words[i].split("/")
            nextWord = next
            finalWord = prevWord + current[0] + nextWord
            finalClass = current[1]
            finalClass = finalClass + " " + finalWord + "\n"
            i +=1
        elif len(words) != 1 :
            prevWord = words[i-1]
            prevWord = words[i-1].split("/")
            prevWord = prev + prevWord[0]
            current = words[i]
            current = words[i].split("/")
            nextWord = words[i+1]
            nextWord = words[i+1].split("/")
            nextWord = next + nextWord[0]
            finalWord = prevWord + current[0] + nextWord
            finalClass = current[1]
            finalClass = finalClass + " " + finalWord + "\n"
            i +=1    
        else:
            current = words[i]
            finalWord  = prev+current[0]+next
            finalClass = current[1]
            i+=1
        f.write(finalClass)
f.close()
#subprocess.call(["/home/ankit/Desktop/csci544-hw2/perceplearn.py",outputPath,"/home/ankit/Desktop/csci544-hw2/pos.nb"])
#os.system("/home/ankit/Desktop/csci544-hw2/perceplearn.py "+outputPath+" /home/ankit/Desktop/csci544-hw2/pos.nb")