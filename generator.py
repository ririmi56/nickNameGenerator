#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

wordsLists = ["adjectivesList.txt", "nounsList.txt"]


def generator():

    words = ""

    for list in wordsLists:

        file = open(list)
        linesNumber = sum(1 for line in file)
        file.close()

        wordNumber = random.randint(0, linesNumber)

        file = open(list)
        for i, line in enumerate(file):
            if i == wordNumber-1:

                words = "{}{}-".format(words, line[:-1], "-")

        file.close()

    return words[:-1]


if __name__ == "__main__":

    a = generator()
    print(a)
