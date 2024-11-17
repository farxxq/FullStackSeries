## Day 5
# Object Oriented Programming

# Classes and objects
print("-----------Classes and objects------------")

# Creating a class
print("#Creating a class")
class TempClass:  # have the name starting with caps (Just a normal rule)
    pass

print(f"The type of Factory: {TempClass}")

# 'Variables' inside a class is called 'Attributes'
# 'Functions' that is created inside a class is called 'Methods'

class Factory:
    print("The factory class")
    a = 10
    b = 20
    def hello():
        print("Hello,from the Function hello() inside the class")

Factory() # used to call the class
print(Factory.a) # to print the values of "a"(attribute) from the class

# hello() # can't call the function as it is in the class instead we use the below one
Factory.hello() # this calls the function in the "Factory" class

# Objects
print("------Objects--------")

class ObjectClass:
    a = 1022004
    b = 28072003

obj = ObjectClass() # this 'obj' is a Object now
print(obj.a) # this prints the values of 'a' (Works as the 'ObjectClass.a')

# Constructors 
# to get the attributes into the class
# In python it is like 'initialization'
print("------Constructors---------")

print("#Constructor1")
class Constructors1:
    # Constructors are called by itself
    def __init__(self):
        print("The Life")

Constructors1() # this calls the function automatically (i.e. we need to call it as "Constructors.__init__()" to actually call it but it calls itself)

print("#Constructor2")
class Constructors2:
    # Constructors are called by itself
    def __init__(self, date, month, year):
        print("The Talk:")
        print(f"The Date: {date}\nThe Month:{month}\nThe Year:{year}")

Constructors2(17,3,2023) # This throws error if the arguments are not given

print("#Constructor3")
class Constructors3:
    # self keyword targets the object
    def __init__(self, date, month, year):
        print(f"The object location: {self}") # This prints the object location (Shows that it targets the location of the objects)
        #This fetches the value of date from the argument given and stores it
        self.date = date 
        self.month = month 
        self.year = year

    def likeMe(self): # this makes it a object method (method - function inside a class, object method - as theLove.likeMe sends the argument(theLove) to the function )
        print("Do you love me? (from likeMe method inside the class)")
        print(f"The date: {self.date}\nThe month: {self.month}\nThe Year: {self.year}")

theTalk = Constructors3(17,3,2023) # this is the object (the class in a var is called a object)
print(f"This fetches the location of theTalk: {theTalk}") #prints the location of the object
print(f"This prints the date from the constructor for theTalk: {theTalk.date}") #prints the value

theLove = Constructors3(19,4,2023) # this is the object (the class in a var is called a object)
print(f"This fetches the location of theLove:{theLove}") #prints the location of the object
print(f"This prints the date from the constructor for theLove: {theLove.date}") #prints the value

# Object Method:
theLove.likeMe() 

# Encapsulation (Keeping the data safe and only authorized people can)
# Eg: In a classroom, Only the people who payed for the class can attend it and the info in that is given only to those inside

print("----Encapsulation----")

class Encapsulation:
    __a = 1
    b = 28
    #public class
    def normalHello():
        print("This is the normalHello function")

    #private class
    #@classmethod # - used to make the next function private
    def __encapHello(): 
        print("This is the encapHello function")

    __encapHello()

print(Encapsulation.b) # gives the value of b
#print(Encapsulation.a) # can't access the var (Interpreter Error: type object 'Encapsulation' has no attribute 'a')

Encapsulation.normalHello() # this calls the function
#Encapsulation.encapHell() # this won't be able to access the function Error shown: type object 'Encapsulation' has no attribute 'encapHell'
Encapsulation() # We can access the function inside that class

# Polymorphism (having many forms)
# Eg: A Mobile phone can be used for many things like (Using Instagram, Camera, Whatsapp, Youtube, Calling)
print("----Polymorphism----")

class Animal:
    def __init__(self,name):
        self.name = name
    def showname(self):
        print(f"The name of the Animal is: {self.name}")

class Human(Animal):
    def showname(self):
        # super().showname() # this will call the stuff from the above class
        print(f"The name of the Human is: {self.name}")

human1 = Human("Faroo")
animal1 = Animal("Tiger")

human1.showname()
animal1.showname()

# Inheritance (Getting the abilities of parents in children)
print("----Inheritance----")

# Life class is called the super class
class Life:
    def __init__(self, date, month, year):
        self.date = date 
        self.month = month 
        self.year = year


#You class
class You:
    def __init__(self,color):
        self.color = color

# Me class is a sub class
class Me(Life,You):
    def __init__(self, date, month, year,day):
        super().__init__(date, month, year) # the Life is the super class
        self.day = day

# We class ....... Multi level inheritance
class We(Me):
    def __init__(self, date, month, year, day,time):
        super().__init__(date, month, year, day)
        self.time = time

obj1 = Me(28,7,2003,"Mon")

print(f"The Date from class Life called through class Me: {obj1.date}")
print(f"The Day from class Life called through class Me: {obj1.day}")

# Abstraction (Only showing the essential stuff)
# Eg: Plug board or switch board (Doesn't show the backend wires connecting it)
print("----Abstraction----")

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Need to make this so that we can access it here
    def area():
        pass

    def perimeter():
        pass

cir1 = Circle(12)


