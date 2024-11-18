# Practicing the concept of Day 5
# Small project kinda using the OOPs concepts

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

