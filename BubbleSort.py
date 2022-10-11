class SortingAlgorithms:
   
  def bubbleSort(self, lst):
    unsortedEnd = len(lst)-1 # variable that represents the end of the unsorted region of the list

    while unsortedEnd > 0:
      for i in range(0, unsortedEnd): # traverse the list from 0 to the end if the unsorted region of the list
        if lst[i] > lst[i+1]: # if the current element is larger than the next element, then swap them
          tmp = lst[i+1]
          lst[i+1] = lst[i]
          lst[i] = tmp
      unsortedEnd -= 1

#Driver code
obj = SortingAlgorithms()
bubbleList = [i for i in range(99, 0, -1)]
obj.bubbleSort(bubbleList)
print(bubbleList)
view raw
