class SortingAlgorithms:
  
  def selectionSort(self, lst):
      for i in range(0, len(lst)-1):
        minIndex = i
        for j in range(i+1, len(lst)): # linearly traverse the unsorted portion of the list searching for the smallest number
          if lst[j] < lst[minIndex]:
            minIndex = j
        tmp = lst[i] # swap the smallest number with the first element in the unsorted region after every linear traversal
        lst[i] = lst[minIndex]
        lst[minIndex] = tmp
        
# Driver code
obj = SortingAlgorithms()
selectionList = [i for i in range(99, 0, -1)]
obj.selectionSort(selectionList)
print(selectionList)
