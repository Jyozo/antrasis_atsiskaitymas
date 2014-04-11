import sys
import os
import re


def read_words(fileName):
    file = open(path+fileName)
    wordcount = {}
    for word in re.findall("[\w']+",file.read()):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def read_symbols(fileName):
    file = open(path+fileName)
    symbolcount = {}
    for symbol in re.findall('\w',file.read()):
        if symbol not in symbolcount:
            symbolcount[symbol] = 1
        else:
            symbolcount[symbol] += 1
    return symbolcount


path = sys.argv[1]

if path[-1] is not '/':
    path = path+'/'

print 'Specified directory: '+path

fileNames = [name for name in os.listdir(path)
             if os.path.isfile(path+name)]

print fileNames

print 'Words from the file '+fileNames[0]
print read_words(fileNames[0])

print 'Symbols from the file '+fileNames[0]
print read_symbols(fileNames[0])
