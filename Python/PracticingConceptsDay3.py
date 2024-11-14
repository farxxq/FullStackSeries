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




