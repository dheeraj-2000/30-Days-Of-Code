#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    name_list = []

    for N_itr in range(N):
        name, mail = input().split()
        if re.search(r'.*@gmail\.com',mail):
            name_list.append(name)
    # . means 'all' in regex so we used \ as an escape sequence
    print(*sorted(name_list), sep ='\n')

