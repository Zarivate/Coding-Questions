# Question:

# Given a non empty array of non negative integers, and a non negative value representing a sum.
# Create a function that find's the longest subarray, inclusive, where the values add up to the target sum 
# and returns an array representing the starting and ending index of the subarray.

# Example:
example_array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
target = 10

# Answer:
# [4, 8]
# 3 + 3 + 1 + 2 + 1 = 10

# Optimal Space & Time Complexity:
# O(n) time | O(1) space
# n = length of array

# Explanation:
# While it would be possible to find the answer by simply going through the array each time for every value until you find
# the right combination, it would result in a time complexity of n^2 so instead what should be kept in mind for this 
# question is how both the target value and the values in the array will always be positive. Using this, and with the help
# of some pointers. You can gradually move them along the array while keeping track of what the current values add up to. 

# Anytime the current sum between the pointers is less than the target value, that's how you would know you have to increment
# the right pointer by 1. As the current sum has to be greater, and because all the values are positive, incrementing the right
# pointer would result in a larget current sum. Anytime the current sum between the pointers is greater than the target value,
# that means you would have to increment the left pointer by 1, as that would make the current subarray smaller, and because
# all the values are positive, by making the subarray smaller you would decrease the current sum. Repeat this until the end of
# the array is reached and return whichever subarray you found was the largest while doing this.


# example_array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
# IE:
# left_pointer = example_array[0] = 1
# right_pointer = example_array[1] = 2
# current_sum = 3
# target = 10
# 3 < 10, 3 is less than 10 so increase the right pointer by 1.

# left_pointer = example_array[0] = 1
# right_pointer = example_array[2] = 3
#**********************************************************************************************
# current_sum = 3 + 3 = 6, current_sum = 6, the previous sum is incremented by the new index value
#**********************************************************************************************
# target = 10
# 6 < 10, 6 is less than 10 so increase the right pointer by 1.

# left_pointer = example_array[0] = 1
# right_pointer = example_array[3] = 4
# current_sum = 6 + 4, current_sum = 10
# target = 10
#**********************************************************************************************
# 10 = 10, target value found so take note of the pointer indexes
# answer_index = [0, 3], length = 4
# Not at end of array so keep going, increment right pointer by 1
#**********************************************************************************************

# left_pointer = example_array[0] = 1
# right_pointer = example_array[4] = 3
# current_sum = 10 + 3, current_sum = 13
# target = 10
# 13 > 10, 13 is greater than 10 so increment left pointer by 1

# left_pointer = example_array[1] = 2
# right_pointer = example_array[4] = 3
# current_sum = 13 - 1, current_sum = 12
# target = 10
# 12 > 10, 12 is greater than 10 so increment left pointer by 1 again

# left_pointer = example_array[2] = 3
# right_pointer = example_array[4] = 3
# current_sum = 12 - 2, current_sum = 10
# target = 10
#**********************************************************************************************
# 10 > 10, target value found so take note of the pointer indexes and compare to previous answer subarray length
# answer_index = [2, 4], length = 3
# answer_index = [0, 3], length = 4
# Not longer than previous subarray, so don't change return answer
# Not at end of array so keep going, increment right pointer by 1
#**********************************************************************************************

# left_pointer = example_array[2] = 3
# right_pointer = example_array[5] = 3
# current_sum = 10 + 3, current_sum = 13
# target = 10
# 13 > 10, greater sum than target value so increment left pointer by 1

# left_pointer = example_array[3] = 4
# right_pointer = example_array[5] = 3
# current_sum = 13 - 4, current_sum = 9
# target = 10
# 9 < 10, smaller sum than target value so increment right pointer by 1

# left_pointer = example_array[3] = 4
# right_pointer = example_array[6] = 1
# current_sum = 9 + 1, current_sum = 10
# target = 10
#**********************************************************************************************
# 10 = 10, target value found, check to see if length of subarray found is greater than previous one
# answer_index = [3, 6], length = 4
# answer_index = [0, 3], length = 4
# Not longer than previous subarray, so don't change return answer
# Not at end of array so keep going, increment right pointer by 1
#**********************************************************************************************

# left_pointer = example_array[3] = 4
# right_pointer = example_array[7] = 2
# current_sum = 10 + 2, current_sum = 12
# target = 10
# 12 > 10, increment left pointer by 1

# left_pointer = example_array[4] = 3
# right_pointer = example_array[7] = 1
# current_sum = 12 - 3, current_sum = 9
# target = 10
# 9 < 10, increment right pointer by 1


#**********************************************************************************************
# left_pointer = example_array[4] = 3
# right_pointer = example_array[8] = 1
# current_sum = 9 + 1 = 10
# target = 10
# 10 = 10, found target sum so check length of subarray
# answer_index = [4, 8], length = 5
# answer_index = [0, 3], length = 4
# Longer than previous subarray, so change return array to [4, 8]
# Keep iterating through array, increment right pointer by 1
#**********************************************************************************************

# left_pointer = example_array[4] = 3
# right_pointer = example_array[9] = 2
# current_sum = 10 + 2 = 12
# target = 10
# 12 > 10, increment left pointer by 1

# left_pointer = example_array[5] = 3
# right_pointer = example_array[9] = 2
# current_sum = 12 - 3 = 9
# target = 10
# 9 < 10, increment right pointer by 1

# At end of array by now, so return stored answer subarray of 
# [4, 8]

# Implementation:
def longestSubWithSum(array, targetSum):
    answer_array = []

    currentSum = 0
    leftPointer = 0
    rightPointer = 0

    while rightPointer < len(array):
        currentSum += array[rightPointer]
        while leftPointer < rightPointer and currentSum > targetSum:
            currentSum -= array[leftPointer]
            leftPointer += 1

        if currentSum == targetSum:
            if len(answer_array) == 0 or answer_array[1] - answer_array[0] < rightPointer - leftPointer:
                answer_array = [leftPointer, rightPointer]

        rightPointer += 1
    
    return answer_array

print(longestSubWithSum(example_array, target))