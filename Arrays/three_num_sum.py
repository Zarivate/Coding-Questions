# Question:
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in array that sum up to target and return a two-dimensional array of these
# triplets.

# Note:
# Both the numbers in each triplet and triplets themselves should be ordered in ascending order with respect
# to the numbers they hold.

# Example:
array_sample = [12, 3, 1, 2, -6, 5, -8, 6]
target_sample = 0

# Answer:
# [ [-8, 2, 6], [-8, 3, 5], [-6, 1, 5] ]

# Optimal Space Time Complexity:
# O(n^2) time
# O(n) space
# n = length of input array

# Explanation:
# The main idea involves first sorting the array, then traversing the array with 2 additional pointers for a total of 3
# numbers being tracked all at once. 1 pointer right after the current position, and the 2nd pointer at the last
# position. At each point, would check to see if all 3 numbers add up to target, if not then move pointers accordingly
# to target. IE, because the array would be sorted, depending on which end has the greatest values, we would only have
# to move the pointers on one of the sorted arrays side.

# Note:
# Sorting the array is an O(n(log(n)) operation but going through the loops in the while loop would be O(n^2)
# which dwarfs it and cause time complexity to be O(n^2)

# Implementation:

