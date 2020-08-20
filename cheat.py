#!/bin/python

from itertools import permutations
import sys

words = []
for line in open('words.txt', 'r').readlines():
    if len(line) > 3 and len(line) < 8:
        words.append(line.rstrip('\n'))


def get_perms(letter_list, word_list):
    spam3 = [''.join(p) for p in permutations(letter_list, 3)]
    spam4 = [''.join(p) for p in permutations(letter_list, 4)]
    spam5 = [''.join(p) for p in permutations(letter_list, 5)]
    spam6 = [''.join(p) for p in permutations(letter_list)]

    results = dict()
    for perm in spam3:
        if perm in word_list:
            if perm not in results:
                results[perm] = None

    for perm in spam4:
        if perm in word_list:
            if perm not in results:
                results[perm] = None

    for perm in spam5:
        if perm in word_list:
            if perm not in results:
                results[perm] = None

    for perm in spam6:
        if perm in word_list:
            if perm not in results:
                results[perm] = None

    return results

letters = input('What are the six letters? ')
match_words = get_perms(letters, words)

while True:
    num = input('How long is the word? (Enter Q to quit.) ')
    if num.lower() == 'q' or num == '':
        sys.exit()
    else:
        try:
            num = int(num)
        except:
            print('Not a valid number')
            continue

    for result in match_words:
        if len(result) == num:
            print(result)