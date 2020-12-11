#!/usr/bin/python3
import sys 
  
print(len(sys.argv),"arguments:") 

if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
       print((idx + 1),":", arg)
