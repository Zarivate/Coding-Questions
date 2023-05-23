# Question

# Write a function that takes in an unordered list of unique integers called "nums" in the range of [1, n], where
# n = len(nums + 2), and returns a new list of the 2 missing numbers sorted numerically.


# Example:

nums_example = [1, 4, 3]
nums_example2 = [1, 4, 3, 5]


# Answer
# [2, 5]
# len(nums_example) = 3, meaning the numbers that could be in the array range from 1-5. The example array is missing
# the 2 and 5 from the given range so return those numbers in an array in ascending order.


# Optimal Space & Time Complexity:
# O(n) time, because will have to iterate through the array
# O(1) space, this is because the new array we create will always have 2 integer values in it. Meaning it will take up
# a total space of O(2) that can be reduced down to O(1) since.


# Explanation:
# The main idea to realize here is how the total sum from both arrays, the one with missing values and one with no
# missing values, can be used to find the missing integers. This is because besides the missing values, the only
# difference between the two arrays will be their sums. IE

# nums_example = [1, 4, 3]
# total = 8 (1 + 4 + 3)

# complete_example = [1, 2, 3, 4, 5]
# total = 15 ( 1 + 2 + 4 + 3 + 5)

# These two totals can them be differentiated and divided by 2 since that's how many numbers we have to find
# 15 - 8 = 7/2 = 3.5, floor it to get 3.

# Because of how the integers are all unique, and the integers increase in ascending order, it would mean that one of the values would need to be greater than it 
# and the other would need to be smaller. This means can divide the potential list of solution integers to this

# [1, 2, 3, 4, 5] is split at the 3 point to get
# [1, 2, 3] and [4, 5]

# Get the sums of these sides of the array
# 6 (1 + 2 + 3) and 9 ( 4 + 5)

# Now can iterate through the main array again and sum up the values according to which side they represent, either
# The left side, that's less than or equal to the dividing value or
# The right side, that's greater than the dividing value

# Once those values are found, they can be subtracted from the original sums of the complete array, the difference will then be the answer
# IE:

# nums_example = [1, 4, 3]
# leftSide = 0
# rightSide = 0

# 1, less than or equal to 3 so add to left side
# leftSide = 1
# rightSide = 0

# 4, greater than 3 so add to right side
# leftSide = 1
# rightSide = 4

# 3, less than or equal to 3 so add to left side
# leftSide = 4
# rightSide = 4

# Now subtract these from the original sums to get the answer
# answer = [6-4, 9-4]
# answer = [2, 5]


# Implementation
def missing_nums(array):
    # Due to how this excludes the last value normally, a + 3 is done so it adds up until the
    # length of the passed in array plus two additional spaces
    total = sum(range(1, len(array)+ 3))

    # Subtract the values in the passed in array from the total
    for value in array:
        total -= value
    
    # Get the subdividing value by dividing the new total by 2 and flooring it
    middle_value = total//2

    # Calculate what the left and right side of the array's totals should be given the found value above
    left_side_goal = sum(range(1, middle_value + 1))
    right_side_goal = sum(range(middle_value + 1, len(array) + 3))

    # Create variables to hold the total sum of the values in the array less than or equal to the medium,
    # and the sum of the values greater than the medium
    left_side = 0
    right_side = 0

    # Iterate through the array again, now while according adding up the values to which side they belong too
    for value in array:
        if value <= middle_value:
            left_side += value
        else:
            right_side += value
    
    # Return the difference between the found totals and the expected totals
    return [left_side_goal - left_side, right_side_goal - right_side]
        

print(missing_nums(nums_example))
print(missing_nums(nums_example2))
