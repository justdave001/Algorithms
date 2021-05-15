#Explanation of the Basic Working Behind Binary Searches

"""
Task: To find the position of a target number in an array
"""
#Array must be sorted to get most accurate results
def binary_search(array, target):

    beginIndex = 0

    endIndex = len(array)

    while beginIndex < endIndex:
        #Get the middle Index of array testspace to see lying area of target number (left/right)
        middleIndex = beginIndex + (endIndex - beginIndex)//2
        
        #To see if target lies to the right then set the beginIndex to the front of prior middleindex
        if array[middleIndex] < target:
            beginIndex = middleIndex + 1

        #To see if To see if target lies to the left then set the endIndex behind middleindex
        #for next iteration
        elif array[middleIndex] > target:
            endIndex = middleIndex - 1

        #Returns position of middleIndex if a match is found
        else:
            return middleIndex
    #if no match is found
    return None
if __name__ == "__main__":
    array = list(map(int, input().rstrip().split()))
    target = int(input())
    print(binary_search(array, target))
        
