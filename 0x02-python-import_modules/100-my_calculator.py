#!/usr/bin/python3
from calculator_1 import *
import sys
""" Write a program that based on value that are passed to param 
make some compute """

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if sys.argv[2] == "+":
    sum = add(int(sys.argv[1]), int(sys.argv[3]))
    print(
        "{} {} {} = {}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sum))
elif sys.argv[2] == "-":
    sub_ = sub(int(sys.argv[1]), int(sys.argv[3]))
    print(
        "{} {} {} = {}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sub_))
elif sys.argv[2] == "*":
    mul_ = mul(int(sys.argv[1]), int(sys.argv[3]))
    print(
        "{} {} {} = {}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        mul_))
elif sys.argv[2] == "/":
    div_ = div(int(sys.argv[1]), int(sys.argv[3]))
    print(
        "{} {} {} = {}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        div_))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
