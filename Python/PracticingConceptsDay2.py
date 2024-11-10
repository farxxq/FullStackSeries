## Some practice questions to understand concepts
## Practicing Concepts Day2
# if-else questions
print("---------if-else questions------------")

# 1. Accept 2 numbers and print the largest among them
print("1. Accept 2 numbers and print the largest among them")

num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")

elif num1 == num2:
    print(f"{num1},{num2} are equal")

else:
    print(f"{num2} is greater than {num1}")

# 2. Accept the gender from the user as char and print the respective greeting message

print("2. Accept the gender from the user as char and print the respective greeting message")

person = input("Enter your Gender:")

if person == "male" or person == "Male" or person == "boy":
    print(f"Assalamwalaikum Sir!")

elif person == "female" or person == "Female" or person == "girl":
    print(f"Assalamwalaikum Mam!")

else:
    print("Wrong input")


# 3. Accept an integer and check whether it is an even number or odd

print("3. Accept an integer and check whether it is an even number or odd")

number = int(input("Enter a number:"))

if number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is a odd number")

# 4. Accept a name and age from the user. Check if the user is a valid voter or not. 

print("4. Accept a name and age from the user. Check if the user is a valid voter or not.")

name = input("Enter your name:")
age = int(input("Enter your age:"))

if age >= 18:
    print(f"{name} is {age} old and is eligible to vote")
elif age < 18 and age > 1:
    print(f"{name} is {age} old and is not eligible to vote")
else:
    print(f"Enter a valid age : {age}")

# 5. Accept a year and verify if it is a leap year or not

print("5. Accept a year and verify if it is a leap year or not")

year = int(input("Enter the year:"))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 6. Accept an English alphabet from user and check if it is a consonant or vowel

print(" 6. Accept an English alphabet from user and check if it is a consonant or vowel")

alphabet = input("Enter an alphabet:")

if alphabet in "aeiouAEIOU":
    print(f"{alphabet} is a vowel")
else:
    print(f"{alphabet} is a consonant")

## Loops Questions

print("---------Loops Questions------------")

# 1. Print natural numbers up to n
print("1. Print natural numbers up to n")

n = int(input("Enter nth number:"))

for i in range (1,n+1):
    # to get the value till n we use n + 1
    print(i) 

# 2. REverse for loop. Print n to 1
print("2. REverse for loop. Print n to 1")

for i in range (n-1,1,-1):
    print(i)

# 3. Take a number as input and print its table
# 5*1 = 5
# 5*2 = 10 ....... upto 10 terms

print("3. Take a number as input and print its table \nEg: 5 * 1 = 5 \n 5 * 2 = 10...... upto 10 terms")

table = int(input("Enter a number for the table:"))

for i in range(1, 11):
    print(f"{table} * {i} = {table * i}")

# 4. Sum up to n terms
# 1+2+3+4 = 10

print("Sum upto n terms \nEg: 1+2+3+4 = 10")

sumNum = int(input("Enter the range of numbers to sum up:"))
sum = 0

for i in range(1,sumNum+1):
    sum = sum + i
    print("sum:",sum)
    print("i:",i)

print(f"The final answer after the sum of {sumNum} is {sum}")

# 5. Factorial of a number

print("Factorial of a number")

factNum = int(input("Enter a Number:"))
fact = 1

for i in range(1,factNum+1):
    fact *= i
    print(fact)

print(f"Factorial of {factNum} is {fact}")

# 6. Print all the factors of a number

print("6. Print all the factors of a number")

factors = int(input("Enter the number:"))

for i in range(1,factors+1):
    if factors % i == 0:
        print(f"{i} is a factor of {factors}")

# 7. Accept a number and check if it is a perfect number or not.
# A num whose sum of factors (excluding the number itself) = Number
# Eg: 6 = 1+2+3

print("7. Accept a number and check if it is a perfect number or not.\nA num whose sum of factors (excluding the number itself) = Number\nEg: 6 = 1+2+3")

perfectNum = int(input("Enter a number:"))

perfectSum = 0

for i in range(1,perfectNum):
    if perfectNum % i == 0:
        perfectSum += i
        print(perfectSum)

if perfectSum == perfectNum:
    print(f"{perfectNum} is a Perfect Number")
else:
    print(f"{perfectNum} is not a Perfect Number")

# 8. Check if the number is prime or not
print("8. Check if the number is prime or not")

primeNum = int(input("Enter a number:"))
count = 0
for i in range(1, primeNum+1):
    if primeNum % i == 0:
        print(f"{i} is the factor of {primeNum}")
        count += 1

if count == 2:
    print(f"{primeNum} is a Prime Number")
else:
    print(f"{primeNum} is a Composite Number")

# 9. Separate each digit of a number and print it on the new line
print("9. Separate each digit of a number and print it on the new line")

newLineNum = int(input("Enter your number:"))

while newLineNum > 0:
    print(newLineNum % 10)

    newLineNum = newLineNum // 10

# 10. Check whether a number is palindrome or  not
print("10. Check whether a number is palindrome or  not")

palin = int(input("Enter your number:"))
copy = palin
palinNum = 0

while palinNum > 0:
    z = palin % 10
    palinNum = palinNum* 10 + z
    palin = palin // 10

print(palinNum)
if copy == palinNum:
    print(f"{copy} is a palindrome number")
else:
    print(f"{copy} is not a palindrome number")

# 11. Check whether a number is strong number or not (Strong number: Addition of the factorials = The Number, Eg: 1! + 4! + 5! = 145)

print(" 11. Check whether a number is strong number or not (Strong number: Addition of the factorials = The Number, Eg: 1! + 4! + 5! = 145)")

strong = int(input("Enter a number:"))
rem = 0
for i in range(1,10):
    fact = strong % 10
    rem = strong // 10
    if rem == 0:
        break
    print(fact)

