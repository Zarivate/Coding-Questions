# Question

# Given an array of unordered positive integers, return the array's majority element without sorting it beforehand and 
# in constant space.

# Example:

example_array = [2, 1, 3, 1, 1, 5, 1]

# Answer
# 3, It appears in 4 of the 7 positions in the array

# Notes:
# A majority element refers to the element that appears in over half of the array.

# Every array will have a majority element

# A majority element is not the same as the element that appears the most often in an array, IE: For arrays of even length that
# have an element that appears in half of the positions doesn't count as the majority element. Like so
# [1, 2, 2, 1] or [3, 3, 3, 2, 5, 6], both have elements (2 and 3 respectively) that appear in half the array but neither 2 or 3 are
# a majority element because they don't appear in over half of the positions of their respective arrays.


# Optimal Space & Time Complexity:
# O(n) time, due to having to iterate through the array at least 1 time
# O(1) space, no extra space used


# Explanation:
# The main idea for this problem is to realize that you'll need to iterate through the array while keeping track of the numnber of
# duplicates you find of the value most likely to be the majority element. Anytime a duplicate value is found, increment the value 
# holding the current number of duplicates of that specific number. Anytime a non duplicate value is found, you can decrement the 
# variable and if it ever reaches 0. That means that the current majority element value can't be correct, and can update it. Like so,

# Breakdown:
# example_array = [2, 1, 3, 1, 1, 5, 1]
# position = 0
# dupes = 0
# majority_element = -1

# Iterate through
# array[position] = array[0] = 2

# dupes = 0, so set the current value to be the most likely majority element
# majority_element = 2
# array[0] = 2 = majority element
# dupes = 1, increment

# Continue
# position = 1
# dupes = 1
# majority_element = 2

# array[1] = 1
# Doesn't match majority element so decrement dupes
# dupes = 0
# Dupes is 0 now so change majority_element value to be 1
# majority_element = 1

# etc

# Bonus fun fact:
# Using the knowledge that every given array will have a majority element, it can be surmised that the majority element would have
# to be within the range of len(array) / 2 + 1. IE: At just over half the positions. This is because in order to have a majority
# element, no values past that point could be the answer due to them not meeting the criteria of needing over half the values. Like so

# example_array = [2, 1, 3, 1, 1, 5, 1]

# The majority element here is 1, which appears within the first 4 postions of this array of length 7. If it were an array like so

# [1, 2, 3, 4, 1, 1, 1]

# The majority element would still be 1, as it appears in over half of the positions. However if it were an array like so

# [1, 2, 3, 4, 5, 5, 5]

# Then there would be no majority element, as 5 is the most common value but doesn't appear in over half the positions. Don't have
# to worry about these cases hoever because the question doesn't allow for these types of arrays to exist as input.


# Implementation:
def majorityElement(array):
    # Create a value to hold however many times a duplicate is found
    dupes = 0
    # Set some value to be the placeholder for the future returned majority element 
    major_element = -1
    # Iterate through the array
    for element in array:

        # If the duplicates value is 0, then means whatever the current majority element value is is wrong, so set the 
        # major element to be the current position value
        if dupes == 0:
            major_element = element

        # If the element matches the current value held as the major element, increment the dupes variable
        if element == major_element:
            dupes += 1
        # Else if means it doesn't match and can decrement it
        else:
            dupes -= 1

    return major_element

print(majorityElement(example_array))