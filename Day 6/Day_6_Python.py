# Enter your code here. Read input from STDIN. Print output to STDOUT

# Let's review

for i in range(int(input())):
    w = input() # Input word
    print(*(''.join(w[::2]),''.join(w[1::2])))

# Using slicing of a string we can achieve the result in minimal lines of code