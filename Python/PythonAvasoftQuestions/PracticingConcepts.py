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

def Factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
        print(f"The factorial of {a} is: {fact}")


userInput = int(input("Enter a number:"))
# PrimeNumber(userInput)
FibonacciSeries(userInput)
# Factorial(userInput)