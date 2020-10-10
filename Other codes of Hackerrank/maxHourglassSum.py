
'''
Problem link : [https://www.hackerrank.com/challenges/2d-array]
Explanation:
Input 6X6 array
Find the max sum among sums of elements of every hourglass 
Each hourglass has 3 rows with 3 , 1 ,3 elements in the first , second and third row respectively
example :
 1 2 3 4 1 6
 1 2 8 4 1 6
 4 7 3 8 1 6
 1 2 3 5 1 6
 4 2 3 4 1 6
 1 2 3 4 1 6

Hourglass : 
1 2 3 
  2
4 7 3
sum of elements of this hourglass= 1+2+3+2+4+7+8

'''
#hourglassSum function returns the maximum sum of hourglasses present in the 6X6 array
def hourglassSum(arr):
 list1=list()
 for r in range(0,4):
  for j in range(0,4):
   s=sum(arr[r][j:j+3])+arr[r+1][j+1]+sum(arr[r+2][j:j+3])      
   list1.append(s)
 return max(list1)
#define empty array arr
arr = []
#input 6X6 array
for _ in range(6):
  arr.append(list(map(int, input().rstrip().split())))
#output
result = hourglassSum(arr)
print("Maximum sum among all hourglasses is : ",result)
