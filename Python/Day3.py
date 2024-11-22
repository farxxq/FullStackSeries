#Day 3
# Functions, Lists, Tuples, Dictionay, Sets

##Functions
print("---------Functions----------")

print("First function")
def firstFunction():
    print("This is a function")

firstFunction()

#Adding parameters to the functions
print("Adding parameters to the functions")
def paraFunction(para):
    print(f"The output got using the parameter: ", para)

paraFunction("Hello, World!")

#Adding more than 2 parameters
print("Adding more than 2 parameters")
def moreParaFunction(para1,para2):
    print(f"This is the Para1: {para1},\nThis is the Para2: {para2}")

moreParaFunction("Hello, Myself first parameter","Myself second parameter")

#Default Parameter
print("Default Parameter")
def defaultParaFunction(para1,para2,para3 = 10):
    print("Sum of the Parameters:",para1+para2+para3)
#default only works if the argument is not sent
defaultParaFunction(1,2)

#Default Arguments
print("Default Arguments")
def defaultArguFunction(para1,para2,para3):
    print("Displaying the paras")
    print(f"This is the 2nd para: {para2}")
    print(f"This is the 3rd para: {para3}")
    print(f"This is the 1st para: {para1}")

defaultArguFunction(para2 = "This is for para2", para1 = "This is for para1", para3 = "This is for para3")

#Return statement in functions
print("Return statement in functions")
def returnFuntion(a):
    if a % 2 == 0:
        return ("Even")
    else:
        return ("odd")
    
#'return' is used to returns the value at the place called whereas the print statement only prints and cannot be used or stored in a variable.
result = returnFuntion(12)
print(f"The result from the function {result}")
    

## Strings
print("--------Strings----------")

#String indexing 
print("String Indexing")

a = "Safar, a KeywOrd"
print(f"Indexing of the {a}: {a[0]}")
print(f"Indexing of the {a}: {a[-14]}")

# String inexing in a range / Slicing
print("String indexing in a range / Slicing")

print("Indexing in a range: ",a[0::2])

# length function
print("Length function")
# len() also considers the spaces
print(f"The lenght of the string : {len(a)}")

# To search each character or the string in a var
print("To search each char in a string")
if "Safar" in a:
    print(True)
else:
    print(False)

# To print character of the string
print("To print each character of the string")
print("using the 'in' keyword")
for i in a:
    print(i)

print("using the 'range' keyword")
for i in range(0, len(a)):
    print(a[i])

# String Methods
print("--------Strings Methods-----------")

print("upper() method")
cap = a.upper()
print(f"This is Capitalized: {cap}")

print("lower() method")
low = a.lower()
print(f"This is lower: {low}")

# To be continued with the string methods refer online documentation

##List
print("------List------")

name = ["Sa", "Fa", "Mu", "Aa", "Fo"]
print(name)

#Mutable (List can be changed)
name[2] = "Muq" # Changes the element in the second index (Mu) to (Muq)
print("The list after updating: ",name)

#List Index
print(f"Printing the index of the list :{name[0]}")

#List slicing
print(f"Slicing of the List elements: {name[0:2:1]}")

#List methods
print("---------List methods--------")
print("insert() method") # to add the element at a particular index
name.insert(5,"Vi")
print("Using the insert() method: ",name)

print("append() method") # to add the element at the end
name.append("Fa") 
print("Using the append() method",name)

print("pop() method")
name.pop() #default the last element is popped
print("The last element is poped",name)
name.pop(5)
print("Popped a particular element",name)

#remove() method
print("remove() method")
name.remove("Aa") #removes the particular element from the list
print("remove() method used:", name) 

#Linear searching in a list 

listSearch = [1,2,2004,28,7,2003]
n = int(input("Enter the element you want to search: "))
index = 0
for i in range(len(listSearch)):
    if listSearch[i] == n:
        index += i
    else:
        pass

print(f"The element {n} is at index : {index}")

##Tuple
print("-------Tuple----------")

bhai = ("Sa", "Mu", "Fou", "Aa", "Vi","Fa",1,2,3)
print(f"The tuple of bhai var is: {bhai} and type is {type(bhai)}")
#Tuple are immutable i.e. we cannot change the values in this tuple

print("Making changes in the tuple despite of them being immutable")

# bhai[2] = "Fa" # Cannot change the value as it is tuple
#instead we can change it to list and then do the operations and then revert it back to tuple

bhai = list(bhai)
print(f"The type of the Bhai is: {type(bhai)} and the list contains: {bhai}")
bhai.insert(5,"Dtr")
print(f"The Bhai list after change: {bhai}")
bhai = tuple(bhai)
print(f"The Bhai tuple after changes: {bhai} and type of bhai is {type(bhai)}")

#To print all the elements
print("Printing each elem using 'range' keyword")

for i in range(len(bhai)):
    print(bhai[i])

print("Printing each elem using 'in' keyword")

for i in bhai:
    print(i)

#Tuple unpacking
print("Tuple unpacking")
tupleEg = ("12","2807","2003")
print(f"The values in the tupleEg: {tupleEg}")
a,b,c = tupleEg # we need to assign all the elems to a variable in the tuple to unpack them
print(f"Prints the value of a as: {a}")
print(f"Prints the value of b as: {b}")
print(f"Prints the value of c as: {c}")

##Sets
print("--------Sets--------")

#Sets need to have unique values and only those will be printed

setEg = {1,2,3,4,"Sa","Fa","Sa","Fa"}

print(f"This is the setEg: {setEg} and the type of it is: {type(setEg)}")

# The indexing can't be used in the sets and also we can't change the values (as we don't know the address of the value stored in the ram)

#print(setEg(0)) #Throws error that it is not callable

eg = [1,2,2,2,3,4,5,5,6,6,6]
print(f"The type of eg: {type(eg)} and the value it has is: {eg}")

eg = set(eg)
print(f"Now the list is changed to set: {type(eg)}, and values: {eg} ")

#Only Using 'in' keyword we can print the elements
print("Only Using 'in' keyword we can print the elements")
for i in setEg:
    print(i)

##Dictionary

print("-------------Dictionary-------------")
#Dictionary has keys and values...... in other language they are said to be 'hashmap' aswell.
dictionary = {
    "Name": "Farooq",
    "Keyword": "Safar"
} 
print(f"This is the dictionary: {dictionary}, type: {type(dictionary)}")
print(dictionary["Name"])

#To make changes we use the keys and not the index
print("To make changes we use the keys and not the index")

dictionary["Name"] = "Faroo"
print(dictionary)

#To make add the elements we need to do as the following
print("To make add the elements")

print(f"The Dictionary: {dictionary}")
dictionary["LoveLang"] = "Urdu"
print(f"The updated dictionary: {dictionary}")

#To add 2 dictionaries
newDict = {1:"Hello",2:"This is",3:"My world!"}

dictionary.update(newDict)

print(f"The updated the value: {dictionary}")

#Printing the dictionary values
print("Printing the dictionary values")
for i in dictionary:
    print(dictionary[i]) #i is the index, that works as keys in dictionary

print("Printing the values of the dictionary using the '.values' keyword")
for i in dictionary.values():
    print(i)

print("Printing the keys of the dictionary using the '.keys' keyword")
for i in dictionary.keys():
    print(i)

import random

random_gen = random.randint(1,100) # this gives a random number between 1 to 100
print(f"This is the random Number generated:{random_gen}")
