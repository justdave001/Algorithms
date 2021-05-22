"""
Sort array using brute force (comparing value in array with sucessive values and then picking the lowest value
"""
#Time complexity = O(n^2)
#Space complexity = O(1)
def selection_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
if __name__ == "__main__":

    array  = list(map(int, input().rstrip().split()))
    print(selection_sort(array))
                
            
