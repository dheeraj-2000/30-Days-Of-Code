year=int(input("enter year"))
if((year%4==0)and(year%100!=0)):
    print(year,"leap year")
elif(year%400==0):
    print(year,"leap year")
else:
    print("not leap year")
