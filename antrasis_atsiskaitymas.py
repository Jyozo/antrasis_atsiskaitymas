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


def get_line(header):
    result = ''
    for x in range(0,len(header)):
        result += '-'
    return result


def write_results(currentFile, header, data):
    currentFile.write(get_line(header)+'\n')
    currentFile.write(header+"\n")
    currentFile.write(get_line(header)+'\n')
    currentFile.write('%-10s %6s \n' % ('Item', 'Frequency'))
    for key, value in data.items():
        currentFile.write('%-10s %6s \n' % (key, str(value)))
    pass


path = sys.argv[1]

if path[-1] is not '/':
    path = path+'/'

fileNames = [name for name in os.listdir(path)
             if os.path.isfile(path+name)]

words = {}
symbs = {}
for fname in fileNames:
    words = dict(Counter(words)+Counter(read_words(fname)))
    symbs = dict(Counter(symbs)+Counter(read_symbols(fname)))

wordHeader = "Words and their frequency in file "
symbHeader = "Symbols and their frequency in file "
newFile = open("Data", "w")
write_results(newFile, "Words from all files", words)
write_results(newFile, "Symbols from all files", symbs)
for fname in fileNames:
    write_results(newFile, wordHeader+fname, read_words(fname))
    write_results(newFile, symbHeader+fname, read_symbols(fname))
newFile.close()
