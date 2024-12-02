## Sorting Algos

commonList = [1,2,2004,28,7,2003]

#Bubble Sorting
def BubbleSort(a):
    print("------Bubble Sorting------")

    for i in range(len(a)):
        isSwap = False # Used to optimize (If the list or the array is sorted it will not run the whole loop i :- (len(bubbleSort)) times)

        for j in range(len(a)-1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                print(f"Swapped: {a[j]} and {a[j+1]}")
                isSwap = True

        if(not isSwap):
            break

        print(f"After Pass {i + 1}: {a}")

    print(f"Sorted List: {a}")

#Selection Sort
def SelectionSort(a):
    print("-----Selection Sort----------")
    for i in range(0,len(a)-1):
        smallIndex = i

        for j in range(i+1,len(a)):
            if a[j] < a[smallIndex]:
                smallIndex = j
        a[i], a[smallIndex] = a[smallIndex], a[i]
        print(f"Pass:{i} \nthe List: {a}")

#Insertion Sort
def InsertionSort(a):
    for i in range(0, len(a)):
        curr = a[i] 
        prev = i-1   
        while (prev >= 0 and a[prev] > curr):
            a[prev + 1] = a[prev]
            prev -= 1
            print(f"\nThe code inside the while loop:\nPrev: {a[prev]}, Prev+1: {a[prev+1]}, Current value: {curr}")
            print(f"The List:{a}")
        a[prev + 1] = curr
        print(f"\nThe code outside the while loop:\nPrev: {a[prev]}, Prev+1: {a[prev+1]}, Current value: {curr}\nList: {a}")
    print("The sorted list:",a)





# BubbleSort(commonList)
# SelectionSort(commonList)
# InsertionSort(commonList)

## Searching Algorithms

# Linear Search
def LinearSearch(a):   
    n = int(input("Enter the element you want to search: "))
    index = 0
    for i in range(len(a)):
        if a[i] == n:
            index += i
    if(n not in a):
        print("The Element is not in list")
    else:
        print(f"The element {n} is at index : {index}")

# Binary Search
def BinarSearch(a):
    pass

LinearSearch(commonList)
