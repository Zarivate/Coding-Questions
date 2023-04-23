# Question:

# Write a function that returns a boolean representing whether a zero-sum subarray exists within a given list
# of integers. A zero-sum subarray is a subarray where all the values add up to 0. As a subarray is any continuous
# section of an array, in the problem a subarray can range in size from 1 element to the size of the entire list.

# Example:
example_list = [-5, -5, 2, 3, -2]


# Answer:
# True (The subarray of [-5, 2, 3] sums up to 0)

# Optimal Space & Time Complexity:
# O(n) time
# O(n) space
# n = length of list/given array

# Explanation:
# What's important to realize is that if a zero-sum subarray does exist in the list, then the continuous sum will at
# some point reappear. IE: Take the example [-5, -5, 2, 3, -2]
# If we keep track of the continuous sum it would look something like this
# [-5, -5, 2, 3, -2]
# -5, -10, -8, -5, -7
# The -5 appears twice, one at the start and then again in the 3rd position. The difference between positions of these
# would be where the subarray is located. Using the idea that, from the 0 position the sum is equal to -5, and that
# from the 0 position to the 3rd position is also equal to -5. IE:
# [-5, -5, 2, 3, -2]
# ->-5
# [-5, -5, 2, 3, -2]
# ----------->-5
# A pseudo formula can be made where, a subarray from 0 to a certain point "x" is equal to a certain sum "s"
# [0, x] = s
# And a subarray from 0 to another point "y" is also equal to the same "s"
# [0, y] = s
# Then can have it so 0 is equal to the x position + 1, up until the new point y
# [x + 1, y] = 0
# Works in the example like so, with the positions
# x = 0
# y = 3
# [1, 3] = 0, -5 + 2 + 3 = 0

# To implement this in code, a set is used as that won't allow for duplicates and can look up and add values in constant
# time on average. Would need to iterate through the list once and populate it with the current running sum of the
# values as you went. If a duplicate sum is ever found, then can return True, else if make it through the whole list
# without finding any duplicate, can return False. It'll be initialized with a value of 0 however, since if a 0 is ever
# found in the list then can immediately return True.

# Implementation:
def zero_sum_subarray(nums):
    # Create a set sum with an initial value of 0
    sums = {0}
    # Create variable to hold running sum
    current_sum = 0
    # Iterate through sent in list
    for num in nums:
        # Increment the running total
        current_sum += num
        # Check it exists in set, if so return True
        if current_sum in sums:
            return True
        # Else if it doesn't exist just add it to the set
        sums.add(current_sum)

    # If make it through whole list without finding a duplicate or 0, can return False
    return False


print(zero_sum_subarray(example_list))