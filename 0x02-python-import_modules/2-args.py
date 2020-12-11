#!/usr/bin/python3
import sys

print(len(sys.argv) - 1, "arguments:")

if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
       print("{:d}: {}".format((idx + 1), arg))
