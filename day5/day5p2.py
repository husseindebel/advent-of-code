#!/usr/bin/python2.7

import re

filename = "day5_input"
nice_string = 0
vowel = r"[aeiou]"

def check_vowels(line):
    num_vowels = 0
    for character in line:
        if re.match(vowel, character):
            num_vowels += 1

    return num_vowels

def letters_in_row(line):
    return re.search(r"([a-z])\1{1}", line)

def contains_strings(line):
    return re.search(r"ab|cd|pq|xy", line)

with open(filename) as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        if contains_strings(line):
            continue
        else:
            num_vowels = check_vowels(line)
            if num_vowels < 3:
                continue
            else:
                if letters_in_row(line):
                    nice_string += 1
                    continue
                else:
                    continue
print nice_string
