#!/usr/bin/python

import sys

file_name = raw_input("Enter file name: ")

if len(file_name) == 0:
    print("Please enter a filename.")
    sys.exit()

file = ''

try:
    file = open(file_name, 'w+')
except IOError:
    print("There was an error reading the file.")
    sys.exit()

file_text = file.read()
sys.exit()


input = raw_input("Enter some content: ")
file_text+=input

file.write(file_text)

print(file.read())
file.close()