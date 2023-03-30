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
    # Create permutations array to hold final answers/combinations
    permutations = []
    permutations_creator(input_array, [], permutations)
    return permutations


def permutations_creator(input_array, current_perm, permutations):
    # If the input array tossed in is empty, and the permutation tossed in isn't, then we've hit
    #  the base case as we're at the end of the array and at the end of one possible combination
    if not len(input_array) and len(current_perm):
        # Add permutation to permutations array
        permutations.append(current_perm)
    else:
        # For loop to go through till the end of the array
        for i in range(len(input_array)):
            # Create a new array to be sent back into the function using the current position
            new_array = input_array[:i] + input_array[i + 1:]
            # Create a new permutation to be sent back into the function using the current position and the previous
            # permutation passed in
            new_permutation = current_perm + [input_array[i]]
            # Call function again
            permutations_creator(new_array, new_permutation, permutations)


# In depth breakdown of above code using array = [1, 2, 3]
# length = 3

# Enter for loop, so start at beginning of array
# i = 0, because i = 0 when the input array is sliced up until position 0, in other words it'll slice everything before
# position 0, which is nothing, so we'll end up with input_array[:i] = []
# input_array[i + 1:] --> input_array[0 + 1:] --> input_array[1:] --> [2,3], will slice from the 1 position until end
# of the array, so we get [2,3]
# new_array = input_array[:i] + input_array[i + 1:] --> [] + [2,3] = [2,3]
# new_permutation = current_perm + [input_array[i]] --> [] + [input_array[0]] --> [] + [1]
# (Because 1 is at the start of the array of [1, 2, 3])
# Call function again, now with permutations_creator(new_array, new_permutation, permutations) -->
# permutations_creator([2,3], [1], [])

# Enter for loop again, now with array of [2,3]
# i = 0, input_array[:i] = []
# new_array = input_array[:i] + input_array[i + 1:] = input_array[:0] + input_array[1:]
# new_array = [] + [3] = [3]
# new_permutation = current_perm + [input_array[i]] --> [1] + [input_array[0]] --> [1] + [2] --> [1,2]
# Call function again, now with
# permutations_creator(new_array, new_permutation, permutations) -->
# permutations_creator([3], [1,2], [])

# Enter for loop again, now with array of [3]
# i = 0, input_array[:i] = []
# new_array = input_array[:i] + input_array[i + 1:] --> input_array[:0] + input_array[1:]
# *************************************************
# new_array = [] + [] = []
# *************************************************
# new_permutation = current_perm + [input_array[i]] --> [1, 2] + [input_array[0]] --> [1, 2] + [3] --> [1,2,3]
# new_permutation = [1,2] + [3] = [1,2,3]
# Call function again, now with
# permutations_creator(new_array, new_permutation, permutations) -->
# permutations_creator([], [1,2,3], [])

# *************************************************
# Enter if check, cause input array is [] while current permutation isn't empty at [1,2,3]
# Add [1,2,3] to permutations array to get
# permutations = [1,2,3]
# *************************************************


# *************************************************
# Increment 1, go back to when input_array = [2,3], current_permutation = [1]
# *************************************************
# i = 1, input array = [2,3]
# new_array = input_array[:i] + input_array[i + 1:] --> input_array[:1] + input_array[2:]
# new_array = [2] + [] = [2]
# new_permutation = current_perm + [input_array[i]] --> [1] + [input_array[1]] --> [1] + [3] --> [1,3]
# new_permutation = [1,3]
# Call function again, now with
# permutations_creator(new_array, new_permutation, permutations) -->
# permutations_creator([2], [1,3], [1,2,3])

# *****************************************
# i = 0 because got reset after calling function again
# *****************************************
# i = 0, input array = [2]
# new_array = input_array[:i] + input_array[i + 1:] --> input_array[:0] + input_array[1:]
# new_array = [] + [] = []
# new_permutation = current_perm + [input_array[i]] --> [1] + [input_array[1]] --> [1,3] + [2] --> [1,3,2]
# new_permutation = [1,3,2]
# Call function again, now with
# permutations_creator([], [1,3,2], [1,2,3])

# *****************************************
# Hit if check, add [1,3,2] to permutations array to get
# permutations =  [1,2,3], [1,3,2]
# Done with all possible combinations where 1 is at start so i = 1 now on first array of [1,2,3]
# *****************************************

# Repeat process, now with i = 1, input_array = 1,2,3], current_perm = [], permutations =  [1,2,3], [1,3,2]
# i = 1, input array = [1,2,3]
# new_array = input_array[:i] + input_array[i + 1:] --> input_array[:1] + input_array[2:]
# new_array = [1] + [3] = [1, 3]
# new_permutation = current_perm + [input_array[i]] --> [] + [input_array[1]] --> [] + [2] --> [2]
# new_permutation = [2]
# Call function again, now with
# permutations_creator([1,3], [2], [[1,2,3], [1,3,2]])

# i = 0, is reset again since called function again, repeat same steps till done


# Optimal Solution:
# Same idea, but now with pointers instead of any array creation/slicing to save space
def get_permutations_optimal(input_array):
    permutations = []
    permutations_creator_optimal(0, input_array, permutations)
    return permutations


def permutations_creator_optimal(i, input_array, permutations):
    if i == len(input_array) - 1:
        permutations.append(input_array[:])
    else:
        for j in range(i, len(input_array)):
            swap(input_array, i, j)
            permutations_creator_optimal(i + 1, input_array, permutations)
            swap(input_array, i, j)


def swap(input_array, i, j):
    input_array[i], input_array[j] = input_array[j], input_array[i]


array = [1, 2, 3]
print(get_permutations(array))
print(get_permutations_optimal(array))
