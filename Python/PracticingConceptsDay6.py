# Searching Algorithms

#Linear Search
listSearch = [1,2,2004,28,7,2003]
n = int(input("Enter the element you want to search: "))
index = 0
for i in range(len(listSearch)):
    if listSearch[i] == n:
        index += i
    else:
        pass

print(f"The element {n} is at index : {index}")