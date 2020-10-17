class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        # We call the parent class's constructor
        self.avg = sum(scores)/len(scores)
        # The parent class's constructor doesn't include scores so we'll add that here
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    
    # Write your function here
    def calculate(self):
        if self.avg <=100 and self.avg >=90:
            return "O"
        elif self.avg <90 and self.avg >=80:
            return "E"
        elif self.avg <80 and self.avg >=70:
            return "A"
        elif self.avg <70 and self.avg >=55:
            return "P"
        elif self.avg <55 and self.avg >=40:
            return "D"
        elif self.avg <40:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())