# Question:
# Given 2 arrays, one holding an array of integers and another holding just 3 distinct integers. The first array will only
# have numbers included within the second, while the second array represents the desired order of the numbers within the first.
# Write a function that sorts the first array so that it's order matches with the desired order within the second.

# Notes:
# No extra space is allowed to be used for this problem.
# Array is allowed to be mutated, IE: Edited in place
# Desired order won't always follow some sort of order like ascending or descending
# While the 1st array will only have numbers within the 2nd, there could be a case where not all the numbers in the 2nd array appear within the 1st


# Example:
example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
order_array = [0, 1, -1]


# Answer:
# [0, 0, 0, 1, 1, 1, -1, -1, -1]


# Optimal Space & Time Complexity:
# O(n) time | O(1) space
# n = number of values in array

# A simple function meant to print out the array to see if the answer is correct
def printOutArray(array):
    for value in array:
        print(value, end=" ")
   

# Explanation:
# The fact that the 1st array will only have numbers found within the 2nd is very important, as it gives a hint that the problem can be
# solved in linear time as it removes any factor regarding unforseen numbers. What it comes down to afterwards is how to keep track of
# the positions where each number should go. While there are many possible solutions for this problem, the ones I'll break down here
# will be answers where only 2 and 1 loop of the array are subsequently needed. Either way pointers will be used to some extent and all
# optimal approaches reduced to the same time and space complexity of O(n) and O(1) respectively. 


# Optimal Answer 1: 2 loops through array
# For this approach the knowledge that the value within the 1st position in the second array, 0, will all be to the far left of the 
# 1st array, and the value within the 3rd position in the second array, -1, will be to the far right of the 1st array. Meaning that if
# these 2 values have their correct positions filled, then the middle value will automatically be within the right places. IE:


# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# order_array = [0, 1, -1]

# Create variables to hold the necessary values:
# first_value = order_array[0] = 0
# last_value = order_array[2] = -1

# These values will hold the index where the values above should be within the 1st array
# first_index = 0
# index_for_last_value = len(example_array - 1) = 8

# Then iterate through the array each time for each value, so 2 times in total, any time you find the corresponding position value in 
# the array, insert it into the position/index of the array. IE:


# Iteration for the first value
# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[0] = 0
# first_value = 0
# first_index = 0

# first_value = example_array[0], so swap positions with first_index, also 0 so nothing really changes
# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# first_index = 1, update the index
# Continue

# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[1] = 1
# first_value = 0
# first_index = 1
# No match so don't swap anything or update index value,
# continue

# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[2] = 1
# first_value = 0
# first_index = 1
# No match so don't swap anything or update index value,
# continue

# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[3] = -1
# first_value = 0
# first_index = 1
# No match so don't swap anything or update index value,
# continue

# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[4] = -1
# first_value = 0
# first_index = 1
# No match so don't swap anything or update index value,
# continue

# **************************************************************************************************
# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# example_array[5] = 0
# first_value = 0
# first_index = 1
# Have match so swap position value in array with wherever the first index is
# example_array = [0, 0, 1, -1, -1, 1, 1, 0, -1]
# Update index value
# first_index = 2
# continue
# **************************************************************************************************


# example_array = [0, 0, 1, -1, -1, 1, 1, 0, -1]
# example_array[6] = 1
# first_value = 0
# first_index = 2
# No match, so don't update anything
# continue,


# **************************************************************************************************
# example_array = [0, 0, 1, -1, -1, 1, 1, 0, -1]
# example_array[7] = 0
# first_value = 0
# first_index = 2
# Have match so swap position value in array with wherever the first index is
# example_array = [0, 0, 0, -1, -1, 1, 1, 1, -1]
# Update index value
# first_index = 3
# continue
# **************************************************************************************************

# Keep iterating through array and find that no more 0s that need to be placed at start of array. Do same process for the third
# position although now from the end of the array till the start, ie: backwards to eventually get the answer.


# Implementation:
# Is slight alteration of explanation above, where instead of doing the first and last values in the order array, you just
# do the first and second since it would result in the same answer.
# Technically O(2n) time since have to iterate through array twice but rounds down to O(n)
def threeNumSort(array, order):
    # Create index value
    index = 0
    # Outer for loop to iterate through array twice
    for i in range(2):
        # Get the corresponding value within the order array
        value = order[i]
        # For loop to iterate through each value in big array, as index is updated can start at that point in future iterations to save some time
        for j in range(index, len(array)):
            # Check to see if the position in the big array matches with the value from the order array
            if array[j] == value:
                # If so swap their places
                array[j], array[index] = array[index], array[j]
                # Update index
                index += 1

    return array

# Works as shown here
print(example_array)
newArray = threeNumSort(example_array, order_array)
printOutArray(newArray)




# Most optimal/1 iteration/big boi solution:

# Explanation:
# This one is a bit more involved pointers wise as it involves only doing 1 iteration through the array but keeping track of all 3 possible
# possible positions simultaneously while only using 2 of the 3 values in the order array. IE:

# Grab the first 2 values of the order array
# firstVal = order[0] = 0
# secVal = order[1] = 1

# Using the knowledge that some values will be all the way at the start and others will be all the way at the end of the array, make
# more variables to hold the possible positions the order values could be in the big array.
# firstIdx, secIdx, thirdIdx = 0, 0, len(array) - 1

# The secIdx is at 0 because the big array isn't guaranteed to have all 3 values in the order array. This will be used to an advantage
# when iterating throug the array.

# Now just iterate through the array but anytime any of the positions match up with any of the values in the order array, swap them
# for their corresponding places. IE:

# firstIdx = F
# secIdx = S
# thirdIdx = T

# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
#                (F,S)                        T
# F = 0
# S = 0
# T = -1
# firstVal = 0
# secVal = 1

# Check to see if the value at S matches up with any of the order values
# S matches with firstVal
# Swap their values, both are 0 so won't change anything though
# example_array = [0, 1, 1, -1, -1, 0, 1, 0, -1]
# Increment both the first and second indexes
# F = 1
# S = 1



def threeNumSortOneIteration(array, order):
    # Grab the first two values in the order array
    firstVal = order[0]
    secVal = order[1]

    # Set the indexes for all three values
    firstIdx, secIdx, thirdIdx = 0, 0, len(array) - 1

    # Until the secIdx, middle position, overtakes the last position, keep iterating through array
    while secIdx <= thirdIdx:
        # Grab the value in the second index
        value = array[secIdx]

        # If the value matches up with the first value 
        if value == firstVal:
            # Swap their positions
            array[secIdx], array[firstIdx] = array[firstIdx], array[secIdx]
            # Increment both indexes
            firstIdx += 1
            secIdx += 1
        # Else if the value matches up with the second value
        elif value == secVal:
            # Just update the second index
            secIdx += 1
        # Else that means the value matches up with the last value in the order array
        else:
            # Meaning you swap the second index with the third index
            array[secIdx], array[thirdIdx] = array[thirdIdx], array[secIdx]
            # Decrement the third index as it starts at the end of the array
            thirdIdx -= 1

    return array