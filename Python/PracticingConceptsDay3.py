## Practicing the concepts Day 3

##Strings

print("---------Strings questions-------")

# 1. Print the string in reverse,in upper,in lower and copy into another string
print("1. Print the string length and in reverse,in upper,in lower and copy into another string")

string = "Hello this is Faroo"

print(f"The string: {string}")

#Length
print("----Length of the string----")
print(f"The length of string: {len(string)}")

#Reverse the string
print("----Reversing the string---")
revString = string[::-1] #Indexing is used in the strings
print(f"The actual string: {string},\nThe reversed string: {revString}")

    #Using for loop
forRevString = ''
for i in range(len(string)-1,-1,-1):
    forRevString += string[i]
print("Reversing using for loop:-")
print(f"The reverse string using for loop: {forRevString}")

# lower string
print("-----Lower string----")
lowerString = string.lower()
print(f"Lower string: {lowerString}")

#Copy
print("----Copy----")
copyString = string
print(f"Copied the string in new var: {copyString}")

# 2. Arrange string characters such that lowercase letters should come first in another string.
print("2. Arrange string characters such that lowercase letters should come first in another string.")

arrangeString = "HELlO hoW aRe YOU"
lowerArrange = ""

# using for loop
for i in arrangeString:
    if i.islower():
        lowerArrange += i

for i in arrangeString:
    if i.isupper():
        lowerArrange += i

print(lowerArrange)

# Using split()
print("Using split() only arranging the one's in the word alone")

arrangeSplit = arrangeString.split() # to split strings into the list
print(f"arrangeSplit: {arrangeSplit}")
result = []
for word in arrangeSplit:
    print("The element in the list is:",word)
    lowerArrangeSplit = ""
    upperSplit = ""
    for char in word:
        if char.islower():
            lowerArrangeSplit += char
            print("LowerSplit:", lowerArrangeSplit)
        elif char.isupper():
            upperSplit += char
            print("UpperSplit:", upperSplit)
        
    sort = lowerArrangeSplit + upperSplit
    print(result)
    result.append(sort)
print(f"Result: {result}")
            
# 3. Count all the letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected outcome: 
# Ṭotal counts of chars, digits and symbols: Chars = 8, Digits = 3, Symbols = 4

print("3. Count all the letters, digits, and special symbols from a given string")

str1 = "P@#yn26at^&i5ve"
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

chars = 0
digits = 0
specialSymbols = 0

#using methods
for i in str1:
    # Python has inbuilt to find whether the char is digit or not..... We need to use ASCII or regExp if we don't use these
    if (i.isdigit()):
        digits += 1
    elif(i.isalpha()):
        chars += 1
    else:
        specialSymbols += 1
print(f"The total number of Chars: {chars},\nDigits: {digits},\nSpecial Symbols: {specialSymbols}.")

# 4. Count the vowels in the string

print("4. Count the vowels in the string")     

vowelStr = "Myself Farooq, How are you doing?"
countVowel = 0
countConsonent = 0
for i in vowelStr:

    if i in "aeiouAEIOU":
        countVowel += 1
    elif(i == " "):
        continue # To avoid spaces from being counted
    else:
        countConsonent += 1

print(f"The Vowels: {countVowel},\nThe Consonents: {countConsonent}")

# Using this in function
print("Usage of functions to find the vowels and consonents")
def vowelCounter(a):
    countVowel = 0
    countConsonent = 0
    for i in a:
        if i in "aeiouAEIOU":
            countVowel += 1
        elif(i == " "):
            continue # To avoid spaces from being counted
        else:
            countConsonent += 1
    return f"The Vowels: {countVowel}\tThe Consonents: {countConsonent}" # This returns the value at the place it is being called

print(vowelCounter(vowelStr)) # Will hold the output here

# 5. Anagram (Palindrome) of the string

print("Anagram(Palindrome) of the string")

string1 = "Mam"
anagram = ""

for i in range(len(string1) - 1, -1, -1):
    string1 = string1.lower()
    anagram += string1[i]

if string1 == anagram:
    print(f"String1 :{string1} and Anagram: {anagram}, Is a palindrome")
else:
    print(f"Not a palindrome, String:{string1} \tAnagram: {anagram}")

## List questions
print("-----List Questions---------")

# 1. Accept the list elements and reprint it.

print("1(a). Accept the list elements and reprint it.")

list1a = []
length = int(input("Enter the number of elements in the list:"))
print("Enter the elements")
for i in range(length):
    elem = input(f"Enter the {i} Element:\t")
    list1a.append(elem)

print(f"The list1 is : {list1a}")

# 1(b). Enter a paragraph and reprint it in the form of list with each word as a separate elem of the list

print("1(b). Enter a paragraph and reprint it in the form of list with each word as a separate elem of the list")

list1b = []
listStr = input("Enter a short paragraph:\t")
listStringb = listStr.split()
print(f"The string in list format: {listStringb}")    

# 2. Print the list elem in reverse order

list2 = [1,2,3,4,5,6]

#Easy method using the python methods
listReverse = list2[::-1]
print(f"The reverse of the list: {listReverse}")

#using for loop
print("Using for loop to reverse")
print(list2)
listReverseLoop = []
for i in range(len(list2)-1,-1,-1):
    listReverseLoop.append(list2[i])

print(f"Reverse of list using for loop: {listReverseLoop}")

# 3. Print the positive and negative numbers of a list in seperate lists
print("3. Print the positive and negative numbers of a list in seperate lists")
list3 = [1,2,3,-4,-5,6,7]
listPos = []
listNeg = []
for i in list3:
    if(i > 0):
        listPos.append(i)
    else:
        listNeg.append(i)

print(f"The Negative elements list: {listNeg}")
print(f"The Positive elements list: {listPos}")

# 4. find the greates element and print its index too.
# [1,96,49,7,2023,2,17,20] => Max Element = 2023, index is 4

print("4. find the greates element and print its index too. \t[1,96,49,7,2023,2,17,20] => Max Element = 2023, index is 4")
list4 = [1,96,49,7,2023,2,17,20,2004,2003]

max = 0
index = 0

for i in range(len(list4)):
    if list4[i] > max:
        max = list4[i]
        index = i

print(f"The largest number is: {max} and \nindex of it is: {index} \nfrom this list: {list4}")

# 5. Find the second largest greatest element and prints it's index too.

print("5. Find the second largest greatest element and prints it's index too.")

list5 = [1,96,49,7,2023,2,17,20,2004,2003]

max = 0
max2 = 0
index = 0
index2 = 0

for i in range(len(list5)):
    if list5[i] > max:
        max2 = max
        index = index
        max = list5[i]
        index = i
    elif list5[i] > max2: # This is used when the element after the max value is less and then greater. (See the list to better understand it)
        max2 = list5[i]
        index2 = i
        
print(f"The second largest number is: {max2} and it's index is : {index2} \nfrom the list:{list5}")

# 6. Check if list is sorted list or not

print("6. Check if list is sorted list or not")

list6 = [1,96,49,7,2023,2,17,20,2004,2003]

#To check whether it is sorted
if not list6 or len(list6) == 1:
    print("The list is either empty or has only 1 value")

for i in range(len(list6) - 1):
    if list6[i] <= list6[i+1]:
        continue
    else:
        print("The list is not sorted")
else:
    print("The list is sorted")


#To sort the unsorted list
if not list6 or len(list6) == 1:
    print("The list is either empty or has only 1 value")

for i in range(len(list6)):
    for j in range(len(list6)-1):
        if list6[j] > list6[j+1]:
            temp = list6[j]
            list6[j] = list6[j+1]
            list6[j+1] = temp

print(f"The list6 is sorted now: {list6}")

# 7. Palindromic list or not, Palindrome means:- Same list even when reversed.

print("Palindromic list or not, Palindrome means:- Same list even when reversed.")

list7 = [1,2,3,4,3,2,1,]
reverseList7 = []

# using the parsing method
if list7[::1] == list7[::-1]:
    print(f"The list: {list7} is Palindromic list according to the parsing method")
else:
    print(f"The list: {list7} is not Palindromic list according to the parsing method")

#using the for loop 
for i in range(len(list7) - 1, -1, -1):
    reverseList7.append(-i)

if list7 == reverseList7:
    print(f"The list: {list7} is a Palindromic list according to the loops")
else:
    print(f"The list: {list7} is not a Palindromic list according to the loops")

# 8. How many seperate elements are there in a list excluding the repetations

list8 = [1,1,1,28,28,28,2,2,7,7,2004,2003,17,3,2023,19,4,2023]
print(f"The number of elements in this list with repeatation :{len(list8)}")
list8 = set(list8)
list8 = list(list8)
print(f"The number of elements in this list without repeatation: {len(list8)}")

## Dictionary Questions
print("-------Dictionary Questions----------")

# 1. Write a dictionary to merge 2 python dictionaries

print("1. Write a dictionary to merge 2 python dictionaries")

dict1a = {
    1: "Sa",
    2: "Far"
}
dict1b = {
    3: "Safar", # need to give different keys if not will override the similar one new value
    4: "<3"
}

dict1c = dict1a
dict1c.update(dict1b)

print(dict1c) #updates the values of dict1a as well
print(dict1a)
#can directly update the stuff aswell using "dict1a.update(dict1b)" without taking the temp var

# 2. Write a code to sum all the values of a dictionary

dict2 = {
    1: 10,
    2: 20,
    3: 30
}
sumDict = 0

for i in dict2:
    sumDict += dict2[i]

print(f"The sum of the elements in the dictionary is: {sumDict}")

# 3. Count the frequency of each element in a dictionary

print("3. Count the frequency of each element in a dictionary")

dict3 = {
    1: 1,
    2: 1,
    3: 28,
    4: 1,
    5: 28,
    6: 2004,
    7: 2003,
    8: 2004,
}

print(f"The dictionary has these values: {dict3}")
countDict = 0

if not dict3:
    print("The Dictionary is empty")
else:
    for i in dict3.values():
            values = i
            print(values)
    
print(f"The number of values repeated in the dictionary are: {countDict}")