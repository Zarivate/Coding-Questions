# Question

# Given a row of seats and a list of constraints, find the most optimal position to sit in. Assuming this row of seats
# is represented as an integer array, where 1s represent filled in seats and 0s represent empty seats,
# return the corresponding index.

# Notes/Constraints:
# May assume the first and last seats are always filled

# Seat must be one that gives the most space, with each side being evenly distributed. IE: In a row of 3 empty
# seats, would like to sit in the middle.

# When there are two equally good seats, return the one with a lower index

# Given array will always have a length of at least 1 and have only 0s and 1s.

# If there is no place to sit, return -1.


# Example:
seats_example = [1, 0, 1, 0, 0, 0, 1]

# Answer:
# 4 (seats_example[4] = 0, is only position that fits constraints since is between an even number of 0s to the left and
# right)


# Optimal Space & Time Complexity:
# O(n) time
# O(1) space
# n = number of seats/length of array


# Explanation:
