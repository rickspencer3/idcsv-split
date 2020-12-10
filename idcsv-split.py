#!/usr/bin/python3

currentTable = 0
currentFile = 0
currentTable = 0

fin = open('my-file.csv')

fout = open('part{}.csv'.format(currentFile), 'a')

line = fin.readline()
while line != None:
    if line.startswith("#group"):
        currentTable += 1
        if currentTable % 100 == 0:
            currentFile += 1
            fout.close()
            fout = open('part{}.csv'.format(currentFile), 'a')
    fout.write(line)
    line = fin.readline()

