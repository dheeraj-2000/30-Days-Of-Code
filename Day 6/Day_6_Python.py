# Enter your code here. Read input from STDIN. Print output to STDOUT

# Let's review

for _ in range(int(input())):
    w = input() # Input word
    print(*(''.join(w[::2]),''.join(w[1::2])))

# Using slicing of a string we can achieve the result in minimal lines of code

# Time complexity: O(n) Because only 1 for loop is iterated n times
# Space complexity: O(n) Because linear heap space is required for the input string
