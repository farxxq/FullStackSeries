# Searching Algorithms

# Linear Search
linearSearch = [1,2,2004,28,7,2003]
n = int(input("Enter the element you want to search: "))
index = 0
for i in range(len(linearSearch)):
    if linearSearch[i] == n:
        index += i
    else:
        pass

print(f"The element {n} is at index : {index}")

# Binary Search

binarySearch = [1,2,3,4,5,6,7]