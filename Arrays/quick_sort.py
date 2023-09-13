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
# L pointer is now past the right pointer, meaning can swap R and P values and start loop all over again on the newly created subarrays
# example_array = [6, 5, 2, 3, 5, 8, 9] 
#                                 P  
# The subarrays created from this was  [6, 5, 2, 3, 5] and [9], and quick sort will be performed on both 
# *************************************************************************************************************************************************


#                  P              R  L


# TODO:
# The rest of this explanation, this is a pain but useful. 