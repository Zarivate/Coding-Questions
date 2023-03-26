# Powerset

# Question:
# Write a function that takes in an array of unique elements (IE: integers, letters, etc), and returns it's powerset.

# Powerset - Set of all subsets,
# IE: powerset of [1,2] is [ [], [1], [2], [1,2] ]

# Notes:
# An empty array can also count as a subset
# Sets in powersets don't have to be in any particular order, IE: [1,2] and [2,1] are considered the same

# Example:
# array = [1,2,3]

# Output = [ [], [1], [2],  [2,1], [3], [3, 1], [3, 2], [3, 1, 2]


# Explanation:
# It's important to notice that the # of sets in the powerset expands exponentially depending on how big the array is.
# The formula is 2^n