#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Split Flux CSV files exported from InfluxDB')
parser.add_argument('filename', type=str, help='The name of the file to split.')
args = parser.parse_args()
filename = vars(args)["filename"]

currentTable = 0
currentFile = 0
currentTable = 0

fin = open(filename)

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

