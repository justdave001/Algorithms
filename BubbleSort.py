# Task: To sort an unsorted array using bubblesort
#Time complexity = O(n^2)
#Space complexity = O(1)

def bubble_sort(inputArr):
    #Declare the array as unsorted
    isSorted = False

    while not isSorted:
"""
      remains true until mismatch found then returns true again
      when all numbers become sorted
"""
       isSorted = True
       for i in range(len(inputArr)-1):
         if inputArr[i] > inputArr[i+1]:
             isSorted = False
             #if number before is larger than number ahead, swap both numbers
             inputArr[i], inputArr[i+1] = inputArr[i+1],inputArr[i]
    return inputArr
if __name__ == "__main__":
     inputArr = list(map(int, input().rstrip().split()))
     print(bubble_sort(inputArr))
             

