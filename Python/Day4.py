#Day 4

## Arrays and it's operations
print("-----------Arrays and it's operations----------")
# Arrays are not a built-in data type but can be created using the array module or libraries like NumPy.

# To create an array we need to import the module first
# The numpy can also be used to make the array 
    #Syntax of it: np.array([1,2,3,4,5])

from array import array

myArray = array('i',[1,2,3,4])

# The below code will display the value of the myArray and not the elements of the array.... We need to change it to list if we need only the elements to display
print(f"myArray = {myArray} and the it's type is {type(myArray)}") 