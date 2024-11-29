# 1.
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

#Input: arr[] = [12, 35, 1, 10, 34, 1]
#Output: 34
#Explanation: The largest element of the array is 35 and the second largest element is 34.
commonList = [1,2,2004,28,7,2003]

def GFG1(arr):
    print("Find the Second Largest in an array")
    print("The list elems:", arr)
    n = len(arr)

    largest = -1
    secondLargest = -1

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest

# print(GFG1(commonList))

   
# 2.
# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
list_with_zeros = [1,0,2,0,2004,28,0,7,0,2003]
list_full_zeros = [0,0,0,0,0,0]
def GFG2(arr):

    print("The list:",arr)

    n = len(arr)

    if 0 not in arr:
        return "No Change in array as there are no 0s."
    
    for i in range(n):
        count = 0
        if arr[i] == 0:
            arr[count],arr[i] = arr[i],arr[count]
            count +=1
            print("The count:",count)
        
    return arr

print(GFG2(list_with_zeros))

