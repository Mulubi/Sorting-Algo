class SortingAlgorithms:
  def quickSort(self, leftIndex, rightIndex, lst) -> int:
      def partition(leftIndex, rightIndex, lst):
        pivotElement = lst[(leftIndex + rightIndex) // 2]
        while leftIndex <= rightIndex:
          # Find element on the left of the partition that is greater than the partitionElement
          while lst[leftIndex] < pivotElement:
            leftIndex += 1
          # Find element on the right of the partition that is less than the partitionElement
          while lst[rightIndex] > pivotElement:
            rightIndex -= 1
          # Perform swap and adjust leftIndex and rightIndex accordingly
          if leftIndex <= rightIndex:
            tmp = lst[leftIndex]
            lst[leftIndex] = lst[rightIndex]
            lst[rightIndex] = tmp
            leftIndex += 1
            rightIndex -= 1
        return leftIndex

      partitionIndex  = partition(leftIndex, rightIndex, lst)
      if leftIndex < partitionIndex - 1:
        self.quickSort(leftIndex, partitionIndex-1, lst)
      if rightIndex > partitionIndex:
        self.quickSort(partitionIndex, rightIndex, lst)
        
# Driver Code
obj = SortingAlgorithms()
quickList = [i for i in range(99, 0, -1)]
obj.quickSort(0, len(quickList)-1, quickList)
print(quickList)
