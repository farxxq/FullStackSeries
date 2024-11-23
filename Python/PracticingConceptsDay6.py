## Sorting Algos

#Bubble Sorting
def BubbleSort(bubbleSort):
    print("------Bubble Sorting------")

    for i in range(len(bubbleSort)):
        isSwap = False # Used to optimize (If the list or the array is sorted it will not run the whole loop i :- (len(bubbleSort)) times)

        for j in range(len(bubbleSort)-1):

            if bubbleSort[j] > bubbleSort[j+1]:
                bubbleSort[j], bubbleSort[j+1] = bubbleSort[j+1],bubbleSort[j]
                print(f"Swapped: {bubbleSort[j]} and {bubbleSort[j+1]}")
                isSwap = True

        if(not isSwap):
            break

        print(f"After Pass {i + 1}: {bubbleSort}")

    print(f"Sorted List: {bubbleSort}")

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




unsortedList = [1,2,2004,28,7,2003]

# BubbleSort(unsortedList)
SelectionSort(unsortedList)








# # Searching Algorithms

# # Linear Search
# linearSearch = [1,2,2004,28,7,2003]
# n = int(input("Enter the element you want to search: "))
# index = 0
# for i in range(len(linearSearch)):
#     if linearSearch[i] == n:
#         index += i
#     else:
#         pass

# print(f"The element {n} is at index : {index}")

# # Binary Search

# binarySearch = [1,2,3,4,5,6,7]
