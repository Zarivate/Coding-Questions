# Question:

# Write a function that takes in an array of integers and returns a sorted version of that array using the Merge Sort
# algorithm. 

# Example:
example_array = [8, 5, 2, 9, 5, 6, 3]

# Answer:
# example_array = [2, 3, 5, 5, 8, 8, 9]

# Optimal Space & Time Complexity:
# Best, Worst, and Average Case:
# O(nlog(n)) time
# O(n) space 
# n = length of input array


# Explanation:
# To start, the unoptimal approach will be detailed out first. This approach involves doing nothing more than doing a simple merge 
# sort algorithm approach with no special adjustments. Split the array in half, creating new arrays, recursively repeat until arrays 
# are of size 1, then gradually create new sorted arrays from the split arrays until new final sorted array is completed, IE: 

# example_array = [8, 5, 2, 9, 5, 6, 3]
# length = 7
# 7/2 rounded down = 3
# Split at the 3 point to get

# left_array = [8, 5, 2, 9], right_array = [5, 6, 3]
# Split once more, beginning with left side as this would be recursive

# left_array = [8, 5, 2, 9]
# length = 4
# 4/2 = 2
# left_array = [8, 5], right_array = [2, 9]
# Split once more, beginning with left side again

# left_array = [8, 5]
# length = 2
# left_array = [8], right_array = [5]

# Arrays are now of size 1, so can go back up and sort them to get
# sorted_array = [5, 8]

# Move back up to right_array = [2, 9] and repeat process
# left_array = [2], right_array = [9]

# Arrays are now of size 1, so can go back up and sort them to get
# sorted_array = [2, 9]

# Now have two sorted arrays of [5, 8] and [2,9]. Repeat sorting process on these and create new array of
# sorted_array = [2, 5, 8, 9]

# Completely done with left side so can repeat process on remaining right side
# right_array = [5, 6, 3]
# length = 3
# 3/2 rounded down = 1

# left_array = [5, 6], right_array = [9]
# Right side is already just 1, but left side is not so repeat process on left side