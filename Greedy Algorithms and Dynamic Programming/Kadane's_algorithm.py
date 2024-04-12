# Question: This can also be known as the, "Max subarray problem"

# Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by adding
# up all the values in a non-empty subarray of the input array.

# Notes:
# A subarray can only contain adjacent numbers for this problem. In other words, only numbers right next to each other
# can be added together for a sum.

# Example:
array_example = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

# Answer:
# 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])


# Explanation:
# While you could do the brute force approach, which would be to sum up all the possible max subarrays at each position,
# that would lead to a time complexity og O(n^2) which wouldn't be optimal. Instead what should be done is to implement
# Kadane's algorithm which would use the previous calculated max subarray sum to find the local max subarray sum. All the
# while a running variable would hold the current greatest max found to later be returned.

# IE:
# array_example = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

# Iterate through like normal
# position = 0
# value = 3
# local_max = 3
# greatest_max = 3

# But at each position, the max would be determined between the local max and the max resulting from adding up
# the local value and the previous one. The greatest_max would only ever be updated if the new local max is
# greater than the current greatest_max. IE:

# position = 1
# value = 5
# local_max = max(5, 3 + 5)
# local_max = 8
# greatest_max = 8

# If the max is greater when the two position values are added up than just the local position by itself, then you
# can increase the size of the subarray to contain the local position. Keep going,

# position = 2
# value = -9
# local_max = max(-9, 8 + -9)
# local_max = -1
# greatest_max = 8

# Keep going
# *****************************************************************************************
# position = 3
# value = 1
# local_max = max(1, -1 + 1)
# local_max = 1
# greatest_max = 8
# *****************************************************************************************

# For cases where the local position value is a greater max than the local and previous values added together,
# reset the subarray to be just the local position value and keep going.

# position = 4
# value = 3
# local_max = max(3, 1 + 3)
# local_max = 4
# greatest_max = 8

# position = 5
# value = -2
# local_max = max(-2, 4 + -2)
# local_max = 2
# greatest_max = 8

# position = 6
# value = 3
# local_max = max(3, 2 + 3)
# local_max = 5
# greatest_max = 8

# position = 7
# value = 4
# local_max = max(4, 5 + 4)
# local_max = 9
# greatest_max = 9

# position = 8
# value = 7
# local_max = max(7, 9 + 7)
# local_max = 16
# greatest_max = 16

# You get the idea, this would continue until eventually reach end of array, by which point the max should be calculated
# and held within some sort of variable. Only being updated once the max itself is overcome. IE:
# array_example = [3, 5, -9, 1, 3, -2, 3, 4,  7,  2, -9,  6,  3,  1, -5,  4]
# max           =  3, 8,  8, 8, 8,  8, 8, 9, 16, 18, 18, 18, 18, 19, 19, 19
# max = 19


# Would break down into 2 scenarios.

# 1. The max is equal to the local max + the local value. IE:
# position = 1
# value = 5
# local_max = max(5, 3 + 5)
# local_max = 8

# 2. The max is equal to the local value, in other words the local value is greater than the local max + local value.
# position = 3
# value = 1
# local_max = max(1, -1 + 1)
# local_max = 1

# Optimal Space & Time Complexity:
# O(n) time, because only iterating through array once
# O(1) space, because not making any extra space that scales with problem


# Implementation:
def max_subarray(array):
    # Set both the local and greatest max to be the start of the array
    local_max = array[0]
    greatest_max = array[0]

    # Iterate through the entire array starting from the 1st position
    for position in range(1, len(array)):
        # Get the current number from the current position in the array
        num = array[position]
        # Calculate the local max by seeing which is greater, the current position value or the current position value + the local max
        local_max = max(num, local_max + num)
        # Calculate the greatest max between the newly calculated local max above and the current greatest max
        greatest_max = max(greatest_max, local_max)

    # Return the greatest max
    return greatest_max

print(max_subarray(array_example))
