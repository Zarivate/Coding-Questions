# Note: Can also be considered a dynamic programming question due to how the answers are coded
# Note: Famous/common interview question

# Question:
# Given a non-empty array of positive integers, where each integer represents the maximum number of steps you can
# take forward in the array, IE: An array of [3,1,5,2,7], where the first position is "3", you can move up to 3
# positions forward in the array, up to the position with a value of "2".

# Write a function that returns the minimum number of jumps needed to reach the final index/last position in the array
# Note: Any jump/move from index "i" to index "i + x" counts as just 1 jump, no matter how big "x" is.

# Example:
# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

# Answer:
# 4 (Because can go from 3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)

# There are 2 ways to go about this, the second is far more clever but difficult to come up with but also more
# efficient.

# 1.
# The first way involves creating another array of equal length to the input array where you would continuously
# update how many jumps would be needed to reach the same point in the input array. The values in the "jump"
# array would be updated by using two separate pointers, 1 for the input array and another for the "jumps" array.
# The pointer for the input array would use value held within the current position to see if it could reach the
# same point + 1 in the jumps array. IE:

# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

# Initialize every index as infinity besides the first position, as that would always take 0 jumps to get to
# jumps = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,]

# Now


# Space Time Complexity
# O(n^2) time (Because have to continuously go over the same positions in the array when updating the jumps array)
# O(n) space (Because would use up extra space of "n" size/input array size when making the jumps array)

# Implementation
def min_jumps(array):
    # Make an array of equal size as input array filled with infinity values
    jumps = [float("inf") for x in array]
    # Initialize first value in jumps array as 0
    jumps[0] = 0

    # For loop to go through outer array
    for i in range(1, len(array)):
        # For loop to go through created jumps array
        for j in range(0, i):
            if array[j] >= i - j:
                jumps[i] = min(jumps[j] + 1, jumps[i])
    # Return last value in jumps array
    return jumps[-1]