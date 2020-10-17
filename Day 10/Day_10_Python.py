#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print(len(max(bin(int(input()))[2:].split('0'))))

''' 
Explanation:
Starting from input

Took an integer input
int(input())

Extracted the binary value of the input
bin(int(input()))
This will give us the binary form of the input with the prefix '0b'

Removing the unwanted prefix '0b'
bin(int(input()))[2:] 

Now we will eliminate all the zeros and separate the consecutive 1s 
bin(int(input()))[2:].split('0')

If the input was 115
Binary = 1110011
So the output of the above line is a list of consecutive ones ['111','11']

Finding the maximum out of the elements we got in the list
max(bin(int(input()))[2:].split('0'))

In the above example 111 is the maximum value

Finding the length of the maximum
len(max(bin(int(input()))[2:].split('0')))

Final step: Print it!
'''
