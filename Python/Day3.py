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

print("Upper() method")
cap = a.upper()
print(f"This is Capitalized: {cap}")

low = a.lower()
print(f"This is lower: {low}")

# to be continued with the string methods

##List
print("------List------")

name = ["Sa", "Fa", "Mu", "Aa", "Fo"]
print(name)

#Mutable (List can be changed)
name[2] = "Muq" 
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

##Tuple
print("-------Tuple----------")
