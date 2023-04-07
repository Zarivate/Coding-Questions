# Question:
# Write a function that takes in two non-empty arrays of integers and determines whether the second array is a
# subsequent of the first. IE: [1, 3, 5] is a subsequence of [1, 3, 7, 5].

# Note:
# Must be in same order in both arrays, else do not count as subsequence.
# IE: [1, 3, 5] isn't a subsequence of [1,5,2,3]

# Example:
sample_array = [1, 9, 5, 2, 6, 4, 0]
sample_subsequence = [9, 2, 6]

# Answer:
# True

# Optimal Space & Time Complexity:
# O(n) time
# O(1) space

# Explanation:
# Main idea involves utilizing pointers for both arrays to increment through both at the same time. A loop of some
# sort will go until the end of either array is reached, and the pointer for the subsequence array will only increment
# if a match is found in the main input array. If no match is found, instead only the pointer in the input array
# is incremented. Once the end of either array is reached, will check to see if the pointer for the subsequence array
# is at the end of the subsequence array, if so that means it was incremented all the way through and all it's values
# were found.


# Implementation:
def valid_subsequence(array, sequence):
    # Initialize values to start at the beginning of both arrays
    array_index = 0
    sequence_index = 0
    # Loop to continue until end of either array is reached
    while array_index < len(array) and sequence_index < len(sequence):
        # Check if their positions have matching values
        if array[array_index] == sequence[sequence_index]:
            # If so increment go to the next value in the sequence array
            sequence_index += 1
        # If not matching, go to the next value in the input array and check if that one matches
        array_index += 1
    # Return whether are at the end of the sequence array, if so means we managed to find all the sequence values
    # in the input array, else if we didn't, means we couldn't and will return False.
    return sequence_index == len(sequence)


print(valid_subsequence(sample_array, sample_subsequence))

# Explanation:
# Same idea as above, only difference is that it's a bit cleaner now. Instead, loop will now only iterate through the
# main input array while moving the pointer for the subsequence array only if a match is found within the input array.


# Implementation:
def valid_subsequence_cleaner(array, sequence):
    # Initialize a starting index for the sequence array
    sequence_index = 0
    # For loop to go through every value in the input array
    for value in array:
        # Check if the value in the sequence array matches the current value in the array
        if sequence[sequence_index] == value:
            # If so go to the next value in the sequence array
            sequence_index += 1
        # Check to see if are at the end of the sequence array
        if sequence_index == len(sequence):
            # If so, means we managed to find all the values in the sequence array in the main array and can return True
            return True
    # If we can't reach end of sequence array by time reach end of main array, means couldn't find all the values and
    # can return False
    return False

print(valid_subsequence_cleaner(sample_array, sample_subsequence))