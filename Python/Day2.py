## Day 2
# Loops and Conditionals in Python

#Conditionals - 
print("-------------Conditionals------------")
# if
a = 10
if(a == 10):
    print(f"a is equal to {a} in if statment") 
    # the f is the format string that is used to show the value of variable inside a string

# if-else

b = "" # the string is empty so answer will be false
if(b): #expects true here
    print("Not Empty in if-else statement")
else:
    print("Empty in if-else statement")

# if-elif-else

if():
    print()
elif ():
    print()
else:
    print()

##Loops
print("-----------Loops-----------")
# for loop:
print("For loops:")
for i in range(1,11):
    print(i)

print("Range thing in loops")
for i in range(1,11,2): 
    #skip the one number
    print(i)

# while loop:
print("While loops")
a = 0
while a < 10:
    print(a)
    a = a+1 # to not get a infinite stuff

#Control Flow:
print("Control flows")

# break
print("Break in for loop")
for i in range(1,21):
    print(i)
    if i == 2:
        break

print("Break in while loop")
b = 0
while b < 10:
    print(b)
    b = b + 1
    if b == 4:
        break

#Continue
print("Continue in for loop")
for i in range(1,21):
    if i == 2:
        # this will skip the 2 and will continue
        continue
    print(i)