#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        lmax = -math.inf
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(0, 4):
        for l in range(0, 4):
            lsum = 0
            for j in range(i, i+3):
                for k in range(l, l+3):
                    if k == l and j == i+1:
                        continue
                    elif k == l+2 and j == i+1:
                        continue
                    else:
                        lsum += arr[j][k]
            #print(lsum)
            if lsum>lmax:
                lmax = lsum
    print(lmax)
