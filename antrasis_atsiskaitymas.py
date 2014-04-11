import sys
import os
import re
from collections import Counter


def read_words(fileName):
    file = open(path+fileName, 'r')
    wordcount = {}
    for word in re.findall("[\w']+", file.read()):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def read_symbols(fileName):
    file = open(path+fileName, 'r')
    symbolcount = {}
    for symbol in re.findall('\w', file.read()):
        if symbol not in symbolcount:
            symbolcount[symbol] = 1
        else:
            symbolcount[symbol] += 1
    return symbolcount


def write_results(currentFile, header, data):
    currentFile.write('------------------------------\n')
    currentFile.write(header+"\n")
    currentFile.write('------------------------------\n')
    currentFile.write('%-10s %6s \n' % ('Item', 'Frequency'))
    for key, value in data.items():
        currentFile.write('%-10s %6s \n' % (key, str(value)))
    pass


path = sys.argv[1]

if path[-1] is not '/':
    path = path+'/'

print 'Specified directory: '+path

fileNames = [name for name in os.listdir(path)
             if os.path.isfile(path+name)]

print fileNames

words = {}
symbs = {}
for fname in fileNames:
    words = dict(Counter(words)+Counter(read_words(fname)))
    symbs = dict(Counter(symbs)+Counter(read_symbols(fname)))

print words
print symbs

newFile = open("Data", "w")
write_results(newFile, "Words from all files", words)
write_results(newFile, "Symbols from all files", symbs)
newFile.close()
