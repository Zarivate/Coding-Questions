# Permutations

# Question:
# Write a function that takes in an array of unique integers and returns an array of all permutations of those
# integers in no particular order

# Notes:
# If input array is empty, should return an empty array

# Example:
# array = [1, 2, 3]

# Output:
# [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]

# Optimal Space & Time Complexity:
# O(n * n!) time
# O(n * n!) space
# n = length of input array
# n! = n factorial = n * (n-1) * (n-2) * (n-3) etc...)

# Explanation:

# The slightly less optimal approach:
# Essentially just iterate through the array, meanwhile swapping numbers accordingly because permutations are
# just different position combinations of the #s in the array, IE:

# [1,2,3], permutations with 1 at the start are
# [1,2,3] and [1,3,2]
# The 2 and 3 simply swapped places, likewise the other permutations are

# [2,1,3] and [2,3,1]
# [3,1,2] and [3,2,1]
# Also follow the same pattern

# This approach follows this idea by using a for loop to iterate through the array, all the while creating a new
# array that helps to create the new permutation in different positions.

# Implementation:
def get_permutations(input_array):
    permutations = []
    permutations_creator(input_array, [], permutations)
    return permutations


def permutations_creator(input_array, current_perm, permutations):
    if not len(input_array) and len(current_perm):
        permutations.append(current_perm)
    else:
        # For loop to go through till the end of the array
        for i in range(len(input_array)):
            print("Input array is " + str(input_array))
            print(input_array[:i])
            print(input_array[i + 1:])
            new_array = input_array[:i] + input_array[i + 1:]
            print("New array is " + str(new_array))
            new_permutation = current_perm + [input_array[i]]
            permutations_creator(new_array, new_permutation, permutations)

# In depth breakdown of above code using
# array = [1, 2, 3]
# length = 3
# i = 0, because i = 0 when the input array is sliced up until position 0, IE: input_array[:i], it won't slice anything,
# and we'll end up with input_array[:i] = []
#


array = [1, 2, 3]
print(get_permutations(array))
