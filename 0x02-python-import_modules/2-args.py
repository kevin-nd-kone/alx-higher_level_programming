#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg == 1:
        print("{:d} {}".format(0, "arguments"))
    elif arg == 2:
        print("{:d} {}".format(1, "argument"))
        for index in range(1, arg):
            print("{:d}: {}".format(arg - 1, sys.argv[index]))
    else:
        print("{:d} {}".format(arg - 1, "arguments"))
        for index in range(1, arg):
            print("{:d}: {}".format(index, sys.argv[index]))
