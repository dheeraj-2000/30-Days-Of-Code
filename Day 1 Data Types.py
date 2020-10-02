import sys


if len(sys.argv) != 4:
    print("must enter 3 values")
    exit(1)

cost = float(sys.argv[1])
tip = float(sys.argv[2])
tax = float(sys.argv[3])

tipPercent = (cost * tip) / 100
taxPercent = (cost * tax) / 100
totalCost = cost + tipPercent + taxPercent
l = totalCost
m = (totalCost * 100) - (1 * 100)
if m >= 50:
    l = l + 1
print(f'The total meal cost is {round(l,2)} dollars.')

