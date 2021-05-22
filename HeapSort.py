def heap_it(arr, n, i):
      #Initialize nth index as largest node 
      largest = i
      l = 2 * i + 1 #to get index of left node
      r = 2 * i + 2 #to get index of right node
  
      #make the largest number parent node
      if l < n and arr[largest] < arr[l]:
          largest = l
    
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # if root isn't largest swap with largest value
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heap_it(arr, n, largest)
  
  
def sort_heap(arr):
      
      #heap from middle to beginning
      for i in range(n//2, -1, -1):
          heap_it(arr, n, i)
  
      for i in range(n-1, 0, -1):
          
          arr[i], arr[0] = arr[0], arr[i]
          heap_it(arr, i, 0)
      return(arr)
  

if __name__ == "__main__":
    
    arr = list(map(int, input().rstrip().split()))
    n = len(arr)
    print(sort_heap(arr))
    
    
