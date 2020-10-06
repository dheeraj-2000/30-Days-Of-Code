"""
Day 9: Recursion - Factorial

Implement the factorial function using recursion.

e.g

1. 3! outputs 6.
2. 5! outputs 120.
3. 1! outputs 1.

Steps
    1. We want to keep breaking down the problem to a simpler base case of when n is 0.
    2. 0! is 1, so we return 1 for when n is 0.
    3. For the remaining function calls we want to return n multiplied by a recursive call to n-1.
    4. For n = 5, in the call stack we would have:
        5 x fact(4)
              4 x fact(3)
                     3 x fact(2)
                            2 x fact(1)
                                  1 x fact(0)
                                          return 1

    5. This results in 5 x 4 x 3 x 2 x 1 = 120.

Time complexity  is O(n) since we make n Recursive calls.
Space complexity is O(h) where h is the height of the function call stack. (h = n)

"""

# Sample Test Case
n = 5

# Code Implementation
def factorial(n):

    if n == 0:    # Base Case
        return 1

    return n * factorial(n-1) # Recursive case
   
        
print(factorial(n)) # Outputs 120


