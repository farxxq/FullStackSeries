# Practicing the concept of Day 5
# Small project kinda using the OOPs concepts

#Question 1:

class Student:
    def __init__(self,rrn,name,dept):
        self.rrn = rrn
        self.name = name
        self.dept = dept
        self.marks = {}

    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f"This {subject} already has marks of {self.marks}")
        else:
            self.marks[subject] = marks

    def avg(self):
        if not self.marks:
            print("There are no marks available")
        total = sum(self.marks.values())
        avg = total/len(self.marks)
        return avg
    
    def display(self):
        print(f"Rrn: {self.rrn}")
        print(f"Name: {self.name}")
        print(f"dept: {self.dept}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks obtained by {self.name} is: {self.avg()}")
        

student1 = Student(96,"Faroo","CSE")
student2 = Student(49,"S","Tech") 

student1.add_marks("Full Stack",90)
student1.add_marks("Ai Chatbot",88)

student2.add_marks("Cancer Bio",99)
student2.add_marks("Data Analytics",95)

student1.display()
student2.display()

## Question 2:
# Create account class with 2 attributes = balance and acc no. 
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
    
    def debit(self,debit_amt):
        self.balance -= debit_amt
        print(f"Money debited {debit_amt}, Your balance is: {self.balance}")

    def credit(self,credit_amt):
        self.balance += credit_amt
        print(f"Money credited {credit_amt},Your balance is: {self.balance}")    

user1 = Account(12345, 100000)
user1.debit(100)
user1.credit(100)
user1.credit(50000)


    

