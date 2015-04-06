# -*- coding: utf-8 -*-

import re
import os

# Get all files in designated path
def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
        elif(os.path.isdir(fppath)):
            files += get_files(fppath)
    return files

# Get the most popular word in designated files
def get_important_word(files):
    worddict = {}
    for filename in files:
        f = open(filename, 'rb')
        s = f.read()
        words = re.findall(r'[a-zA-Z0-9]+', s)
        for word in words:
            worddict[word] = worddict[word] + 1 if word in worddict else 1
    wordsort = sorted(worddict.items(), key=lambda e:e[1], reverse=True)
    return wordsort

if __name__ == '__main__':
    files = get_files('.')
    print files
    print get_important_word(files)