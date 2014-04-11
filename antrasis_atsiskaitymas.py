import sys
import os
import re
from collections import Counter


#Scans for words and their frequency in a file
def read_words(fileName, path):
    file = open(path+fileName, 'r')
    wordcount = {}
    for word in re.findall("[\w']+", file.read()):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


#Scans for symbols and their frequency in a file
def read_symbols(fileName, path):
    file = open(path+fileName, 'r')
    symbolcount = {}
    for symbol in re.findall('\w', file.read()):
        if symbol not in symbolcount:
            symbolcount[symbol] = 1
        else:
            symbolcount[symbol] += 1
    return symbolcount


#Returns a string with the same length as given argument
def get_line(header):
    result = ''
    for x in range(0, len(header)):
        result += '-'
    return result


#Writes data into a file, adds formatting
def write_results(currentFile, header, data):
    currentFile.write(get_line(header)+'\n')
    currentFile.write(header+"\n")
    currentFile.write(get_line(header)+'\n')
    currentFile.write('%-10s %6s \n' % ('Item', 'Frequency'))
    for key, value in data.items():
        currentFile.write('%-10s %6s \n' % (key, str(value)))
    pass


#Prints help lines
def print_help():
    print '-----HELP-----'
    print 'Give this program a directory as the first parameter to ' \
          'get a file containing the statistics of all the files ' \
          'present in the directory.'
    print 'Example: '+__file__+' /example/directory/'
    print '--------------'
    pass


#Primitive argument scanning
def parse_args():
    if len(sys.argv) < 2 or (sys.argv[1] == '?'):
        print_help()
        sys.exit()
    else:
        return sys.argv[1]


#Fixies simple human mistakes
def fix_path(path):
    if path[-1] is not '/':
        path = path + '/'
    if path[0] is not '/':
        path = '/' + path
    return path


#Main flow of the script
def main():

    #Variables/constants
    path = fix_path(parse_args())
    words = {}
    symbs = {}
    wordHeader = 'Words and their frequency in file '
    symbHeader = 'Symbols and their frequency in file '

    #Getting a list of file names in the specified directory
    fileNames = [name for name in os.listdir(path)
                 if os.path.isfile(path+name)]

    #Collecting statistics of all the files
    for fname in fileNames:
        words = dict(Counter(words)+Counter(read_words(fname, path)))
        symbs = dict(Counter(symbs)+Counter(read_symbols(fname, path)))

    #Creating a new file and writing the data
    newFile = open("Statistics", "w")
    write_results(newFile, "Words from all files", words)
    write_results(newFile, "Symbols from all files", symbs)
    for fname in fileNames:
        write_results(newFile, wordHeader+fname,
                      read_words(fname, path))
        write_results(newFile, symbHeader+fname,
                      read_symbols(fname, path))
    newFile.close()

    pass


if __name__ == "__main__":
    main()
