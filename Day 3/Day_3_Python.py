#!/bin/python3

import math
import os
import random
import re
import sys

def Type_Number(n):
    if n%2 != 0:
        print("Weird")
    if n%2 == 0:
        if (n>20):
            print("Not Weird")
        elif (n>=6):
            print("Weird")
        elif (n>=2):
            print("Not Weird")
        

if __name__ == '__main__':
    N = int(input())
    Type_Number(N)

