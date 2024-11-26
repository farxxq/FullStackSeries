## Avasoft Prepration

# Prime Number:
def PrimeNumber(primeNum):
    count = 0
    for i in range(1, primeNum + 1):
        if primeNum % i == 0:
            print(f"{i} is the factor of {primeNum}")
            count += 1

    if count == 2:
        print(f"{primeNum} is a Prime Number")
    else:
        print(f"{primeNum} is a Composite Number")

#Fibonacci Series:
def FibonacciSeries(a):
    n1,n2 = 0,1
    for i in range(a):
        print(f"{n2}")  
        n1, n2 = n2, n1 + n2

#Factorial:
def Factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
        print(f"The factorial of {a} is: {fact}")


# userInput = int(input("Enter a number:"))
# PrimeNumber(userInput)
# FibonacciSeries(userInput)
# Factorial(userInput)

list1 = [1,96,49,7,2023,2,17,20,2004,2003] 

#Sum of the elements in the list
def SumOfElem(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    print("The whole sum of the list:", sum)
# SumOfElem(list1)

#Max and minimum Elements in a list

def MaxNMin(a):
    min_val = a[0]
    max_val = a[0]
    for i in range(0, len(a), 1):
        if a[i] > max_val:
            max_val = a[i]
            
        if a[i] < min_val:
            min_val = a[i]
           
    print(f"The final max value is: {max_val}")
    print(f"The final min value is: {min_val}")
# MaxNMin(list1)


# Find the length of the list
def LengthList(a):
    print("First Approach:\nThe lenght of the list is:", len(a))
    count = 0
    for i in a:
        count += 1
    print("Second Approach:\nThe lenght of the list is:", count)
LengthList(list1)

# Swap first and the last element of the list
def SwapElems(a):
    #first approach
    a[0],a[-1] = a[-1],a[0]
    print("First Approach:\nThe List after swap:",a)

    print("\nList Before Second Approach:", a)
    temp = a[0]
    a[0] = a[-1]
    a[-1] = temp
    print("Second Approach:\nThe list after swap:",a)


SwapElems(list1)

