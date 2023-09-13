# Question:

# Given an array of integers, write a function that returns it sorted through the Quick Sort method. 

# Example:

example_array = [8, 5, 2, 9, 5, 6, 3]

# Answer:
# example_array = [2, 3, 5, 5, 6, 8, 9]



# Explanation:
# The question is honestly pretty straight forward. The tricky part just comes from implementing quick sort and having to explain the time and space
# complexities accompanying it.


# Breakdown:
# Quick sort works by selecting a pivot within the array, then two other pointers that represent all the values that should go to the left of the pointer
# and all numbers that should go to the right. These pointers are normally on opposite ends and represent the values less than and greater than the pivot
# respectively. The pivot will be at the start of the array, and the left and right pointers will be on opposite ends. Comparisons will be made to see 
# whether the left and right pointers' value correspond correctly to where they should be. IE: All left pointer values should be less than the pivot
# and all right pointer values should be greater. In cases where this isn't the case, adjustment and swaps are made accordingly like so


# example_array = [8, 5, 2, 9, 5, 6, 3] 
#                  P  L              R
# P = Pivot
# L = Left pointer
# R = Right pointer

# P = 8
# L = 5
# R = 3
# L is 5, 5 < 8, left values should be less than the pivot so this is correct
# R is 3, 3 < 8, right values should be greater than the pivot so this is wrong and should be swapped, but not until an incorrect L value is found
# Keep R pointer where it is, move L pointer up by 1
# Continue

# example_array = [8, 5, 2, 9, 5, 6, 3] 
#                  P     L           R
# L = 2, 2 < 8, left value still less than pivot so keep moving along
# Move L pointer by 1 and continue

# *************************************************************************************************************************************************
# example_array = [8, 5, 2, 9, 5, 6, 3] 
#                  P        L        R
# L = 9, 9 > 8, left values should be less than the pivot this is not the case here so can now swap values with R and decrement R pointer by 1
# example_array = [8, 5, 2, 3, 5, 6, 9] 
#                  P        L     R
# *************************************************************************************************************************************************
#  Continue

# example_array = [8, 5, 2, 3, 5, 6, 9] 
#                  P        L     R
# L = 3, 3 < 8, left values should be less than pivot so this is correct
# R = 6, 6 < 8, right values should be greater than pivot so this is incorrect, keep moving L pointer by 1 until find incorrect L value

# example_array = [8, 5, 2, 3, 5, 6, 9] 
#                  P           L  R
# L = 3, 5 < 8, left values should be less than pivot so this is correct, keep moving L pointer

# example_array = [8, 5, 2, 3, 5, 6, 9] 
#                  P              R
#                                 L
# L = 6, 6 < 8, left values should be less than pivot so this is correct, keep moving L pointer


# *************************************************************************************************************************************************
# example_array = [8, 5, 2, 3, 5, 6, 9] 
#                  P              R  L
# L pointer is now past the right pointer, meaning can swap R and P values and start loop all over again on the newly created subarrays.
# The reason P and R can be swapped willingly is because, once the L passes R, R is guaranteed to be smaller than the pivot and since the pivot
# is at the start of the array, it doesn't change anything when comparisons are done later.
# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                                 P  
# The subarrays created from this was [6, 5, 2, 3, 5] and [9], and quick sort will be performed on both. Will first be done on smaller subarray so it
# can finish first and save space on the call stack and then on the bigger array. Although since the smaller subarray is just of size 1 don't really 
# have to do quick sort on it. 
# *************************************************************************************************************************************************

# Now quicksort would be done on the bigger array just like normal.
# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                  P  L        R
# P = 6
# L = 5
# R = 5
# L is 5, 5 < 6, left values should be less than the pivot so this is correct
# R = 5, 5 < 6, right value should be greater than the pivot so this is wrong, keep R here and keep incrementing the L pointer until find an L value greater than the pivot

# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                  P     L     R

# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                  P        L  R

# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                  P           R
#                              L

# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                  P           R  L

# Never found a left pointer value greater than the pivot, the L is now past the R meaning swap R and P and repeat quick sort process on even smaller subarrays
# example_array = [5, 5, 2, 3, 6, 8, 9] 

# example_array = [5, 5, 2, 3, 6, 8, 9] 
#                  P  L     R 
# P = 5
# L = 5, 5 = 5, left values should be less than or equal to the pivot so this is fine, move pointer by 1 now
# R = 3, 3 < 5, right values should be greater than pivot so this is wrong, keep pointer here, and move L pointer till find incorrect L value

# example_array = [5, 5, 2, 3, 6, 8, 9] 
#                  P     L  R 

# example_array = [5, 5, 2, 3, 6, 8, 9] 
#                  P        R 
#                           L 

# example_array = [5, 5, 2, 3, 6, 8, 9] 
#                  P        R  L

# Didn't find incorrect L value before L crosse R, meaning can swap P and R and start again
# example_array = [3, 5, 2, 5, 6, 8, 9] 
#                  P  L  R  
# P = 3
# L = 5, 5 > 3, L values should be less than the pivot so this is wrong, keep L pointer here for now
# R = 2, 2 < 3, R values should be greater than pivot so this is also wrong, keep R pointer here
# Have case where both L and R pointers are wrong so can swap their values

# example_array = [3, 2, 5, 5, 6, 8, 9] 
#                  P  L  R  
# L = 2, 2 > 3, L values should be less than pivot so correct, can move L pointer forward
# R = 5, 5 > 3, R values should be less than pivot so correct, can move R pointer left

# example_array = [3, 2, 5, 5, 6, 8, 9] 
#                  P  R  L  
# L pointer has crossed R, so can swap the R and P values to get

# example_array = [2, 3, 5, 5, 6, 8, 9], by now should see this is sorted but also because the subarray of [2] is also size of just 1, so should know it's sorted


# Space and Time Complexity:
# Best Case:
# O(log(n)) space | O(n(log(n))) time
# Average:
# O(log(n)) space | O(n(log(n))) time
# Worst Case:
# O(log(n)) space | O(n^2) time
#  n = length of input array

# Time Explanation:
# Best and Average:
# When a quick sort is done the array will be split into subarrays of varying sizes that can be quickly sorted due to being progressivly
# smaller and faster to perform quick sort on. IE: After a quick sort on an array of [x, y, z, a, b, c, q, v] results in [x, y, z, a, v, c, q, b], 
# the subarrays could be something like [x, y, z, a] and [c, q, b]
# And could get progressivly smaller, resulting in an n operation being performed log(n) times


# Worst case:
# This is because, on average, input arrays won't be in an order that will require quick sort to be performed on each value in the array, IE: A case
# where the pivot and R pointer swapping results in the pivot moving to the end of the array and R to the start like the example array. In otherwords
# the subarrays created from the swaps wouldn't be of size 1 and n-1, n-2, n-3, etc. 

# In the worst case where this is the case, quick sort is performed on nearly every value of the array, resulting in iterating through n-1, n-2, n-3, 
# which just rounds down to n values, n times. Resulting in n^2.

# Space Explanation:
# Regardless, so long as quick sort is performed on the smaller subarray first and finishes it's recursive calls before perfoming quick sort on the larger
# subarray, the call stack should never exceed a space of log(n).



# Implementation:
def quickSort(array):

    # Simple helper function to make things cleaner
    quickHelper(array, 0, len(array) - 1)
    return array

# Helper function that does the actual quick sorting, takes in the array, which will always be the same size, but the pointers passed in will determine
# how far and for how long the sorting will last.
def quickHelper(array, startPointer, endPointer):
        
        # If ever a case where the startPointer exceeds and or is equal to the end, means entire array has been sorted and can return
        if startPointer >= endPointer:
              return
        
        # Creat the necessary pointers from the passed in values
        pivotPointer = startPointer
        leftPointer = startPointer + 1
        rightPointer = endPointer

        # So long as the leftPointer doesn't overtake the rightPointer, iterate through the array
        while rightPointer >= leftPointer:
            # If the leftPointer value is greater than the pivot, and the rightPointer value is less than the pivot, then that means both positions
            # are wrong and their values can be swapped
              if array[leftPointer] > array[pivotPointer] and array[rightPointer] < array[pivotPointer]:
                    array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
            # If
              if array[leftPointer] <= array[pivotPointer]:
                    leftPointer += 1
              if array[rightPointer] >= array[pivotPointer]:
                    rightPointer -= 1
        
        # Once out of while loop, means leftPointer has overtaken right and can swap the pivotPointer value with the rightPointerValue
        array[pivotPointer], array[rightPointer] = array[rightPointer], array[pivotPointer]
        
        # Check to see whether the subarray formed on the left side is smaller than what's on the right side
        leftSubarraySmaller = rightPointer - 1 - startPointer < endPointer - (rightPointer + 1)

        # If so, then perform quickSort on the left side, the smaller subarray, first and then the larger one on the right
        if leftSubarraySmaller:
              quickHelper(array, startPointer, rightPointer - 1)
              quickHelper(array, rightPointer + 1, endPointer)
        # Else, perform quick sort on the right side, which in this case would be the smaller subarray, first and then the left side
        else:
              quickHelper(array, rightPointer + 1, endPointer)
              quickHelper(array, startPointer, rightPointer - 1)


# A simple function meant to print out the array to see if the answer is correct
def printOutArray(array):
    for value in array:
        print(value, end=" ")


# Display results, before and after sorting
printOutArray(example_array)
quickSort(example_array)
print()
printOutArray(example_array)