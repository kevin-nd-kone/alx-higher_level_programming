#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None
    if sentence == "":
        return length, first_char
    length = len(sentence)
    first_char = sentence[0]
    return length, first_char
