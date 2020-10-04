import sys

listOfValues = []
n = 0
numSwaps = 0
if len(sys.argv) != 2:
    print(f'Enter the number of elements to sort')
    exit(1)
else:
    n = int(sys.argv[1])

for i in range(n):
    temp = input('Enter value to be sorted: ')
    listOfValues.append(int(temp))

for i in range(n):
    for j in range(n-1):
        if listOfValues[j] > (listOfValues[j+1]):
            tmp = listOfValues[j]
            listOfValues[j] = listOfValues[j+1]
            listOfValues[j+1] = tmp
            numSwaps += 1
    if numSwaps == 0:
        exit(0)

print(f'Array is sorted in {numSwaps} swaps.')
print(f'First Element: {listOfValues[0]}')
print(f'Last Element: {listOfValues[-1]}')
