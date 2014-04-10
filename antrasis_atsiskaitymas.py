import sys
import os


def read_words(fileName):
    file = open(path+fileName)
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


path = sys.argv[1]

if path[-1] is not '/':
    path = path+'/'

print 'Specified directory: '+path

fileNames = [name for name in os.listdir(path)
             if os.path.isfile(path+name)]

print fileNames

print 'Words from the file '+fileNames[0]
print read_words(fileNames[0])
