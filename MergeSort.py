#From Medium

class SortingAlgorithms:
  
  def mergeSort(self, lst):
      if len(lst) > 1:
        # Split part of the algorithm
        middle = len(lst) // 2 # floor division to find middle of the list
        leftList = lst[:middle]
        rightList = lst[middle:]
        self.mergeSort(leftList) # left side of the list
        self.mergeSort(rightList) # right side of the list

        leftIndex = rightIndex = mergedIndex = 0

        # merge part of the algorithm
        while leftIndex < len(leftList) and rightIndex < len(rightList):
          if leftList[leftIndex] < rightList[rightIndex]:
            lst[mergedIndex] = leftList[leftIndex]
            leftIndex += 1
          else:
            lst[mergedIndex] = rightList[rightIndex]
            rightIndex += 1
          mergedIndex += 1
        # Ensure the remaining elements of either leftList or rightList are appended to the end of lst
        while leftIndex < len(leftList):
          lst[mergedIndex] = leftList[leftIndex]
          leftIndex += 1
          mergedIndex += 1
        while rightIndex < len(rightList):
          lst[mergedIndex] = rightList[rightIndex]
          rightIndex += 1
          mergedIndex += 1
        
# Driver code
obj = SortingAlgorithms()
mergeList = [i for i in range(99, 0, -1)]
obj.mergeSort(mergeList)
print(mergeList)


#From DigitalOcean

def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2  # Finding the mid of the array
        left = unsorted_array[:mid]  # Dividing the array elements
        right = unsorted_array[mid:]  # into 2 halves

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1


# Code to print the list
def print_list(array1):
    for i in range(len(array1)):
        print(array1[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(array)
    merge_sort(array)
    print("Sorted array is: ", end="\n")
    print_list(array)
