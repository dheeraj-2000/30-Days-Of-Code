""""
Q.25: RUNNING TIME AND COMPLEXITY
Objective -
Today we're learning about running time! 
Task - 
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Given a number,n, determine and print whether it's Prime or Not.

Note: If possible, try to come up with a O√n primality algorithm, 
or see what sort of optimizations you come up with for an O(n) algorithm.
Be sure to check out the Editorial after submitting your code!

"""
import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False

    return True


p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);