#Day 4

## Arrays and it's operations
print("-----------Arrays and it's operations----------")
# Arrays are not a built-in data type but can be created using the array module or libraries like NumPy.

# To create an array we need to import the module first
# The numpy can also be used to make the array 
    #Syntax of it: np.array([1,2,3,4,5])

# i - integerType - 2 bytes
# f - floatType - 4 bytes
# d - floatType - 8 bytes
# u - unicodeChar - 2 bytes

from array import array

myArray = array('i',[1,2,3,4])

# The below code will display the value of the myArray and not the elements of the array.... We need to change it to list if we need only the elements to display
print(f"myArray = {myArray} and the it's type is {type(myArray)}") 

# To take the element values from the user
import numpy as np
userInput = int(input("Enter the Number of Elements in the list: ")) # taking input from the user for the list 
arr1 = []# creating empty list for now then convert it to array

for i in range (0,userInput):
    elem = int(input("Enter your list element: "))
    arr1.append(elem)# appending the values of munnu in nunu
print(arr1)

arr1 = np.array(arr1)

print(f"The array: {arr1} and it's type: {type(arr1)}")
