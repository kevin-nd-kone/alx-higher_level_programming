#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv)
    s = 0
    for num in range(1, arg):
        argument = sys.argv[num]
        if argument.isdigit():
            s += int(sys.argv[num])
    print(s)
