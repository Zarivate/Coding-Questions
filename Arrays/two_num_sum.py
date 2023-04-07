# Question:
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two integers in the input array add up to the target sum, the function should return then in an array, in
# any order. If no two numbers add up to the target value, the function should return an empty array.

# Note:
# Target sum can't be obtained by adding the same value twice, has to be 2 distinct integers in the array.
# Can assume there will be at most 1 pair of numbers that add to target

# Example:
array_sample = [3, 5, -4, 8, 11, 1, -1, 6]
target_sample = 10


# Answer:
# [-1, 11]

# Many possible solutions, will list them out from least to most optimal

# Least Optimal:
# Space & Time Complexity:
# O(n^2) time (Due to having to go through entire array at each value/character)
# O(1) space

# n = length of input array

# Explanation:
# Main idea is, for every number/position in the array, all subsequent positions will be checked to see if they add
# up to the target value. This is accomplished with a double for loop.

# Implementation:
def two_num_sum_unoptimal(array, target_sum):
    # Outer for loop to iterate until end of array
    for i in range(len(array) - 1):
        # Variable to hold current value in position
        first_num = array[i]
        # Inner for loop that goes until end of array, don't have to do until -1 of array length here because,
        # inner for loop is 1 ahead of outer, so if did -1 then when outer for loop is at second to last position,
        # inner loop wouldn't be able to reach end because len(array) - 1 would prevent it from doing so.
        for j in range(i + 1, len(array)):
            # Variable to hold second value in following position
            second_num = array[j]
            # Check if sum of two variables is equal to target
            if first_num + second_num == target_sum:
                # If so return them
                return [first_num, second_num]
    return []


print(two_num_sum_unoptimal(array_sample, target_sample))


# More Optimal (Time wise) Hashtable method:
# Space & Time Complexity:
# O(n) time
# O(n) space (Due to hashtable creation that at most could be of n/input array size)


# Explanation:
# Main idea revolves around the concept of being able to figure out the potential matching number for the target
# sum using the equation of target = x + y, which because we'll have at least 1 value when iterating through the
# array, we can transform into y = target - x.
# IE:
# array_sample = [3, 5, -4, 8, 11, 1, -1, 6]
# target_sample = 10
# 10 = x + y
# If we were to iterate through the array, we would have something like
# 10 = 3 + y
# Which could be transformed into
# y = 10 - 3 = 7 --> y = 7
# Now all we would have to do is see if 7 exists in the array, but that could involve bloating the time complexity
# to O(n^2) so instead a Hashtable is created, that has a constant look up time (O(1)), that'll hold the values
# we know exist in the table and will be referenced when checking if the calculated value exists.
# IE:
# Continuing off the previous example, our hashtable would look like this at the start when we look to see if we have 7
# {}
# we see that it's empty, so after the first example it would have
# {3: True}
# Now if we keep this up we would do something like this
# y = 10 - 5 = 5 --> y = 5
# Check to see if 5 exists in hashtable
# {3: True}
# Doesn't so keep going and update Hashtable to be
# {3: True, 5: True}
# Etc.


# Implementation:
def two_num_sum_optimal_time(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []


print(two_num_sum_optimal_time(array_sample, target_sample))


# Most Optimal Approach (Space wise)

# Space & Time Complexity:
# O(n(log(n)) time (Due to sorting array and iterating through it)
# O(1) space (Because no auxiliary space


# Explanation:
# Main idea is to first sort the array, that way the values are in order, and then to use two pointers. One
# at the start of the array and another at the end of the array. Sum the two positions up and depending on
# whether the sum is greater than or less than the target sum, the pointers are moved accordingly. Once an
# equal sum is found, the two values are returned. If no match is found, an empty array is returned.


# Implementation:
def two_num_sum_optimal_space(array, target_sum):
    array.sort()
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer < right_pointer:
        current_sum = array[left_pointer] + array[right_pointer]
        if current_sum == target_sum:
            return [array[left_pointer], array[right_pointer]]
        elif current_sum < target_sum:
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
    return []


print(two_num_sum_optimal_space(array_sample, target_sample))
