class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        # Add some more code to run some checks on initialAge
        if self.initialAge<0:
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        if (self.initialAge<18 and self.initialAge>=13):
            print("You are a teenager.")
        elif (self.initialAge<13):
            print("You are young.")
        else:
            print("You are old.")

        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.initialAge = self.initialAge+1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")