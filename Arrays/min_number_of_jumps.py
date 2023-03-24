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

# Now start at the 1st position in the main array, i=1 and array[i] = 4

# Set a pointer for the jumps array to 0, j = 0
# Check to see if you can jump from index j all the way up to index i, in other words can you go from the first
# position in the array to the second using the value of array[j] = array[0] = 3? Yes we can, so we would update
# the value in the corresponding position in the jump array, i position/1 position, from inf to 1 because when
# comparing which one is smaller between "inf"/jumps[i] and jumps[j] + 1 (it would be + 1 because it would take
# us 1 more jump than what we had before in the jumps array)

# jumps = [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf,]

# Repeat the process, once again checking for all values that come before the one we're currently at "i". If we find we
# can make the jump from j to i, using whatever value is within array[j], then we update the value in jump[i] to
# whichever one is smaller, the value already held within jump[i] or the previous position in the jump array + 1
# IE:
# i = 2, array[i] = array[2] = 2
# j = 0, array[j] = array[0] = 3
# Can go from array[j] up to array[i]?
# array[j] = 3, so have 3 jumps and i-j = 2 - 0 = 2
# (the distance between the positions, can it be cleared by the value within array[j]?)
# Yes because 3 > 2, now can update corresponding position in jumps array, jumps[i] = jumps[2] = inf
# Which one is smaller?
# inf or jumps[j] + 1 = jumps[0] + 1 = 0 + 1 = 1?
# 1 is smaller so now we have

# jumps = [0, 1, 1, inf, inf, inf, inf, inf, inf, inf, inf,]

# Keep going, now accounting for the values that go up to i/come before it
# i = 2, array[i] = array[2] = 2
# j = 1, array[j] = array[1] = 4
# Can go from array[j] up to array[i]?
# array[j] = 4, so have 4 jumps and i-j = 2 - 1 = 1
# (the distance between the positions, can it be cleared by the value within array[j]?)
# Yes because 4 > 1, now can update corresponding position in jumps array, jumps[i] = jumps[2] = 1
# Which one is smaller?
# 1 or jumps[j] + 1 = jumps[1] + 1 = 1 + 1 = 2?
# 1 is smaller, so we don't change anything we still have

# jumps = [0, 1, 1, inf, inf, inf, inf, inf, inf, inf, inf,]

# By thi point j would increment to 2, which would catch up to i which means we increment i now and do it all again
# i = 3, array[i] = array[3] = 1
# j = 0, array[j] = array[0] = 3
# Can go from array[j] up to array[i]?
# array[j] = 3, so have 3 jumps and i-j = 3 - 0 = 3, just enough jumps
# (the distance between the positions, can it be cleared by the value within array[j]?)
# Yes because 3 >= 3, now can update corresponding position in jumps array, jumps[i] = jumps[3] = inf
# Which one is smaller?
# inf or jumps[j] + 1 = jumps[0] + 1 = 0 + 1 = 1?
# 1 is smaller, so we have

# jumps = [0, 1, 1, 1, inf, inf, inf, inf, inf, inf, inf,]
# You get the idea by now hopefully

# Space Time Complexity
# O(n^2) time (Because have to continuously go over the same positions in the array when updating the jumps array/at
# every index, will iterate through every index before it.
# O(n) space (Because would use up extra space of "n" size/input array size when making the jumps array)

# Implementation
def min_jumps(array):
    # Make an array of equal size as input array filled with infinity values
    jumps = [float("inf") for x in array]
    # Initialize first value in jumps array as 0
    jumps[0] = 0

    # For loop to go through outer array
    for i in range(1, len(array)):
        # For loop to go through created jumps array, will go up to whatever the i value is
        for j in range(0, i):
            # If we find that the jump position in the input array, a value farther ahead than in the jumps array,
            # is greater than the difference between the two positions, we see if we can update the corresponding
            # i position in the jumps array
            if array[j] >= i - j:
                # Check to see which value is lower and update corresponding position in the jumps array
                jumps[i] = min(jumps[j] + 1, jumps[i])
    # Return last value in jumps array
    return jumps[-1]


# 2.
# The second possible way involves only 1 pointer, but now we keep track of the farthest point you can reach
# alongside whenever a jump is required. IE:

# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

# Use the first value (i) in the array, so index 0 = array[0] = 3
# Means we have 3 steps
# Means we can go up to array[3]

# steps = 3
# maxReach = array[3]

# Use another pointer to iterate through the array, all the while decrementing our steps, checking to see if
# a new maxReach is possible and if we ever run out of steps, then we know we'll have to jump no matter what. IE:
# Increment through the array with a second pointer 1 ahead of starting point, so at index 1.

# ***************************
# Note: Would only need to go up to the second to last point in the array when incrementing through it,
# because by then we could just return however many jumps we calculated + 1 as it would only take 1 more
# step to get through to the end at that point. Example shown near the end
# ***************************

# j = 1, array[j] = array[1] = 4
# maxReach = array[j] + j = 4 + 1 = 5, (+1 because have to account for current index)
# maxReach = max of either array[3] or array[5]
# maxReach = array[5]
# steps -= 1, steps = 2
# steps isn't 0 yet so no jump necessary

# Keep going
# j = 2, array[2] = array[2] = 2
# maxReach = array[j] + j = 2 + 2 = 4, (+2 now because are at 2nd index)
# maxReach = max of either array[5] or array[4]
# maxReach = array[5] still, no change
# steps -= 1, steps = 1
# steps isn't 0 yet so no jump necessary

# Keep going
# j = 3, array[3] = array[3] = 1
# maxReach = array[j] + j = 1 + 3 = 4, (+3 now because are at 3rd index)
# maxReach = max of either array[5] or array[4]
# maxReach = array[5] still, no change
# steps -= 1, steps = 0
# Steps is 0 now, so we increment some sort of jump variable by 1
# jumps += 1 = 1
# Reset steps to be the difference between the farthest point and the current index, as that would be the
# distance before we would need to jump again. In other words we would have
# steps = maxReach - current index
# steps = 5 - 3 = 2

# Keep going
# j = 4, array[j] = array[4] = 2
# maxReach = array[j] + j = 2 + 4 = 6,
# maxReach = max of either array[5] or array[6]
# maxReach = array[6]
# steps -= 1, steps = 1
# steps isn't 0 yet so no jump necessary

# Keep going
# j = 5, array[j] = array[5] = 3
# maxReach = array[j] + j = 3 + 5 = 8,
# maxReach = max of either array[6] or array[8]
# maxReach = array[8]
# steps -= 1, steps = 0
# Steps is 0 now, so we increment some sort of jump variable by 1
# jumps += 1 = 2
# Reset steps to be the difference between the farthest point and the current index, as that would be the
# distance before we would need to jump again. In other words we would have
# steps = maxReach - current index
# steps = 8 - 5 = 3

# Keep going
# j = 6, array[j] = array[6] = 7
# maxReach = array[j] + j = 7 + 6 = 13,
# maxReach = max of either array[8] or array[13]
# maxReach = array[13]
# steps -= 1, steps = 2

# Keep going
# j = 7, array[j] = array[7] = 1
# maxReach = array[j] + j = 1 + 7 = 8,
# maxReach = max of either array[8] or array[13]
# maxReach = array[13]
# steps -= 1, steps = 1

# Keep going
# j = 8, array[j] = array[8] = 1
# maxReach = array[j] + j = 1 + 8 = 9,
# maxReach = max of either array[9] or array[13]
# maxReach = array[13]
# steps -= 1, steps = 0
# Steps is 0 now, so we increment some sort of jump variable by 1
# jumps += 1 = 3
# Reset steps to be the difference between the farthest point and the current index, as that would be the
# distance before we would need to jump again. In other words we would have
# steps = maxReach - current index
# steps = 13 - 8 = 5

# **********************************************************
# Keep going
# j = 9, array[j] = array[9] = 1
# maxReach = array[j] + j = 1 + 9 = 10,
# maxReach = max of either array[10] or array[13]
# maxReach = array[13]
# steps -= 1, steps = 4

# By now we're at the second to last place in the array, in other words
# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1 (right here), 3]
# All we would have to do at this point is return whatever jump we calculated + 1 because no matter what, all it
# would take is 1 more jump to reach the last point. Also to account for any situations where the maxReach is out
# of bounds in the array like it was here. So
# return jumps + 1
# **********************************************************


# Space Time Complexity:
# O(n) time (as would still need to iterate through the array 1 time to get answer)
# O(1) space (not creating any extra space that scales with the size of the input like in the first example)

# Implementation
def min_jumps_optimal(array):
    if len(array) == 1:
        return 0

    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1

example_array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(min_jumps(example_array))
print(min_jumps_optimal(example_array))
