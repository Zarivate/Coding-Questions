# Question:

# Given a non empty array of non negative integers, and a non negative value representing a sum.
# Create a function that find's the longest subarray, inclusive, where the values add up to the target sum 
# and returns an array representing the starting and ending index of the subarray.

# Example:
example_array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
target = 10

# Answer:
# [4, 8]
# 3 + 3 + 1 + 2 + 1 = 10

# Optimal Space & Time Complexity:
# O(n) time | O(1) space
# n = length of array

# Explanation:
# While it would be possible to find the answer by simply going through the array each time for every value until you find
# the right combination, it would result in a time complexity of n^2 so instead what should be kept in mind for this 
# question is how both the target value and the values in the array will always be positive. Using this, and with the help
# of some pointers. You can gradually move them along the array while keeping track of what the current values add up to. 

# Anytime the current sum between the pointers is less than the target value, that's how you would know you have to increment
# the right pointer by 1. As the current sum has to be greater, and because all the values are positive, incrementing the right
# pointer would result in a larget current sum. Anytime the current sum between the pointers is greater than the target value,
# that means you would have to increment the left pointer by 1, as that would make the current subarray smaller, and because
# all the values are positive, by making the subarray smaller you would decrease the current sum. Repeat this until the end of
# the array is reached and return whichever subarray you found was the largest while doing this.


# example_array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
# IE:
# left_pointer = example_array[0] = 1
# right_pointer = example_array[1] = 2
# current_sum = 3
# target = 10
# 3 < 10, 3 is less than 10 so increase the right pointer by 1.

# left_pointer = example_array[0] = 1
# right_pointer = example_array[2] = 3
#**********************************************************************************************
# current_sum = 3 + 2 = 5, current_sum = 5, the previous sum is incremented by the new index value
#**********************************************************************************************
# target = 10
# 5 < 10, 5 is less than 10 so increase the right pointer by 1.




# Implementation: