#importing array library to use reverse function
from array import *
#creating array
mylist=[]
#taking number of inputs from user
n=int(input(""))
#taking array elements from user and appending them to array
for i in range(0,n):
    temp=int(input(""))
    mylist.append(temp)
#reversing array using reverse() function already defined in 'array' library
mylist.reverse()
#display array elements in reverse order
print(str(mylist))


