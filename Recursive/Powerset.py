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
# The formula is 2^n, so if an array has
# 3 elements? There are 2^3 = 8 combinations IE: [1,2,3] --> Example above
# 2 elements? There are 2^2 = 4 combinations IE: [1,2] --> [ [], [1], [2], [1,2] ]
# 1 elements? There are 2^1 = 2 combinations IE: [1] --> [ [], [1] ]
# 0 elements? There are 2^0 = 1 combinations IE: []

# ********************************************
# To actually make the sets in the powerset, what you have to do is take all the previous sets and
# add the following element to it:
# IE: [1,2] --> [ [], [1], [2], [1,2] ]
# [] is given cause empty array makes empty set
# [1] is just 1 added to empty set of before
# [2] is just 2 added to empty set of before
# [1,2] is just 2 added to [1] of before
# ********************************************

# Optimal Space Time Complexity:
# O(n * 2^n) time
# This is for the same reason as below, everytime you append that's an operation of that on average
# are of length n/2, which reduces down to just "n".
# IE: Take [1,2,3] -- > [ [], [1], [2],  [2,1], [3], [3, 1], [3, 2], [3, 1, 2]
# At most these sub arrays are of length "n", and at least they are of length 0. In between these two of length
# 0 and N, we have most of the arrays which are of around length n/2 that reduces to n

# O(n * 2^n) space
# This is because 2^n is the total number of subsets we'll have in our return array, while "n" comes from
# the average size off the subsets being n/2 which reduces down to just "n"


# Solutions, one is iterative while the other is recursive. Iterative is just easier to understand
def powerset_iteratively(input_array):
    # Create an empty subsets array with only an empty array
    subsets = [[]]
    # Iterate through every element in the input array
    for element in input_array:
        # At every element, iterate up until the length of the declared subsets array
        for i in range(len(subsets)):
            # Locate the current array/array at position "i" in the declared subsets array
            current_subset = subsets[i]
            # Add a new subset to the subsets array, consists of the current subset + whatever element currently at
            subsets.append(current_subset + [element])

    # Once finished and gone through every element in the input array, return the subsets array
    return subsets


# On first call, idx is not going to be passed in, so it's initialized to None to avoid having to do any slicing
# business when recursively calling the function, as slicing an array is an O(n) operation since essentially copying it
def powerset_recursively(input_array, idx=None):
    # If the index is none/null, then start at the last index/element of the array
    if idx is None:
        idx = len(input_array) - 1
    # Base case where index becomes negative
    if idx < 0:
        return [[]]
    # Locate the current element at the current index in the input array
    element = input_array[idx]
    # Call the function again, but this time on the index before the last one. Goes off the idea that
    # the power set of any array is just the previous subset + the last element. IE:
    # Powerset of [1,2,3] is the powerset of [1,2] with 3 added to every element
    subsets = powerset_recursively(input_array, idx - 1)
    # Same idea as in iterative solution, iterate till end of subsets
    for i in range(len(subsets)):
        # Find the current subset in the subset array
        current_subset = subsets[i]
        # Append a new subset to the subsets array that consists of the current subset + whatever element currently at
        subsets.append(current_subset + [element])
    # Return created subsets array
    return subsets

# Bonus walkthrough of recursive solution, take [1,2] as input array
# Idx starts as None, so would hit if check and make idx = 1, cause length of [1,2] is 2
# element = 2 --> input_array[1] --> [1,2] --> 2
# subsets = powerset_recursively(input_array, idx - 1) --> subsets = powerset_recursively([1, 2], 0)
# element = 0 --> input_array[0] --> [1,2] --> 1
# subsets = powerset_recursively(input_array, idx - 1) --> subsets = powerset_recursively([1, 2], -1)
# idx = -1, -1 < 0 so hit if check and return [[]]

# Go back to subsets = powerset_recursively([1, 2], -1) call with [[]] returned
# subsets = [[]]
# Go to for loop, for i in range(len(subsets)) --> for in in range(0)
# current_subset = subsets[i] --> current_subset = [[]]
# subsets.append(current_subset + [element]) -- > [1] --> [[], [1]]

# Go back to subsets = powerset_recursively([1, 2], 0) call with [[], [1]] returned
# subsets = [[], [1]]
# Go to for loop, for i in range(len(subsets)) --> for in in range(0)
# current_subset = subsets[0] --> current_subset = [[], [1]] --> current_subset = [[]]
# subsets.append(current_subset + [element]) -- > [2] --> [[2]]
# Go to for loop, for i in range(len(subsets)) --> for in in range(1)
# subsets.append(current_subset + [element]) -- > [2] --> [[1,2]]
# subsets = [[], [1], [2], [1,2]]


array = [1, 2, 3]
print(powerset_iteratively(array))
print(powerset_recursively(array))
