import os
import sys
import re
import random

inputPath = sys.argv[1]
outputPath = sys.argv[2]

#to read the total classes
classes = []

#to get the name of .nb file
f = open(inputPath,"r")
lines = f.readlines()
f.close()
#-------------------------

#To get the names of all possible classes
for line1 in lines:
    line = re.sub("[\n+]","",line1)
    line = re.sub("\s+"," ",line)
    words = line.split(" ")
    if words[0] not in classes:
        classes.append(words[0]) 
#-------------------------

#to store the weight  vectors for all the classes
weightVectors = {}

# declare initital dictionaries for classes
for _class in classes:
    weightVectors[_class] = {}
#----------------------

for line in lines:
    line = re.sub('\s+',' ',line)
    words =  line.split(' ') 
    for word in words:
        if word not in words[0]:
            for _class in classes:
                if word not in weightVectors[_class]:
                    #print(word+" ")            
                    weightVectors[_class][word] = 0
                    

#print(str(len(weightVectors['HAM'])) + " " + str(len(weightVectors['SPAM'])))


'''for _class in classes:
    for key,value in weightVectors[_class].items():
        print(_class + " " + key + " " + str(value))'''
 
for i in range(15):       
    random.shuffle(lines)
    for line in lines:
        featureVector = {} # to store feature vector for current line    
        weightsCount = {} # to store .product for each class
        maxClassValue = 0  #store max count out of all the classes
        maxClassName = '' # classname for the preditiob
        
        line = re.sub('\s+',' ',line)
        words = line.split(' ')
            
        for word in words: #to get the feature vector
            if word not in words[0]:
                if word not in featureVector:
                    featureVector[word] = 1
                else:
                    featureVector[word] += 1
        
        for _class in classes: # initialize class weight. This will be . product
            weightsCount[_class] = 0
            
        for _class in classes: # calculate weightCount
            for word in words:
                if word not in words[0]:
                        weightsCount[_class] = weightsCount[_class] + weightVectors[_class][word]#*featureVector[word]
                        #weightsCount[_class] = weightsCount[_class] + 1
                
        
        maxClassValue = weightsCount[classes[0]]
        maxClassName = classes[0]
        
        for _class in classes: #predict class depending upont maxClassValue
            if weightsCount[_class] > maxClassValue:
                maxClassValue = weightsCount[_class]
                maxClassName = _class
        
        if i == 14:
            print('P ' + maxClassName + ' D ' + words[0])  #testing
        
        '''for _class in classes: #testing
            for item,value in  weightVectors[_class].items():
                print(item + " " + str(value)) '''
                
        if maxClassName not in words[0]:
            for word in words:
                if word not in words[0]:
                    #weightVectors[words[0]][word] = weightVectors[words[0]][word] + featureVector[word] 
                    weightVectors[words[0]][word] = weightVectors[words[0]][word] + 1
            

f = open(outputPath,"w")


for key, value in weightVectors[classes[0]].items():
    fileLine = key
    for _class in classes:
        fileLine = fileLine + " " + _class + " " +  str(weightVectors[_class][key])
    fileLine = fileLine + "\n"
    f.write(fileLine)
f.close();

'''for key,value in weightVectors.items():
    print(key + " " + str(value))'''
            
            
                 