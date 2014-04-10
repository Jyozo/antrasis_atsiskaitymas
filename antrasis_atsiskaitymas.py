import sys
import os


def read_words():
    pass

path = sys.argv[1]

if path[-1] is not '/':
    path = path+'/'

print 'Einamasis katalogas: '+path

fileNames = [name for name in os.listdir(path)
             if os.path.isfile(path+name)]

print fileNames
