#!/usr/bin/python2.7

import re

filename = "day5_input"
nice_string = 0

def first_condition(string):
    return re.search(r"([a-z]{2}).*\1{1}", string)

def second_condition(string):
    return re.search(r"([a-z]).{1}\1{1}", string)

with open(filename) as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        if first_condition(line):
            if second_condition(line):
                nice_string += 1
            else:
                continue
        else:
            continue

print nice_string
