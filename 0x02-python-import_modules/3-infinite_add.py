#!/usr/bin/python3
import sys
if __name__ == "main":
    arg = len(sys.argv)
    s = 0
    for num in range(1, arg):
        code = code(sys.argv[num])
        if code.isdigit():
            s += int(sys.argv[num])
    print(sum)
