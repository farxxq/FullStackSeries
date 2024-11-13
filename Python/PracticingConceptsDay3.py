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
print("Using split()")

arrangeSplit = arrangeString.split()
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
            



