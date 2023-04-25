# Question:

# Given an array of buildings and the direction they're facing, return an array of the indices of the buildings that
# can see the sunset.

# Notes:
# Returning answer array should be sorted in ascending order
# A building can only see the sunset if it's taller than all the buildings that come after it in the pointing direction.
# The buildings array at the current index, sample_buildings[i], represents that buildings height
# The direction will either be "EAST" or "WEST"

# Example:

sample_buildings = [3, 5, 4, 4, 3, 1, 3, 2]
sample_direction = "EAST"

# Answer:
# [1, 3, 6, 7]

# Example 2:
sample_buildings2 = [3, 5, 4, 4, 3, 1, 3, 2]
sample_direction2 = "WEST"


# Answer:
# [0, 1]

# Optimal Space & Time Complexity:
# O(n) time
# O(n) space
# n = length of input array

# Explanation:
# This is a case where there are various best case solutions, for now the non stack will be explained.
# Essentially what's important to keep in mind if not using a stack for the solution is how the maximum height of the
# buildings in the path of the current building is what determines whether it can see the sunset or not. Using this
# info, if you iterate in the opposing direction and keep track of the current tallest building height, you can then
# use that to compare to the current building's height. If the current building's height is taller than the current
# maximum found height, then it can view the sunset and be added to the solution array to be returned. IE:

# sample_buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# sample_direction = "EAST" (-->)

# Initialize some value to hold the maximum running height to 0
# max_height = 0
# Direction is "EAST" so start at end of array

# sample_buildings[7] = 2
# 2 > 0, so add to answer array
# answers = [7]
# update max height, max_height = 2

# sample_buildings[6] = 3
# 3 > 2, so add to answer array
# answers = [7, 6]
# max_height = 3

# sample_buildings[5] = 1
# 1 < 3, so don't add to answer array
# answers = [7, 6]
# max_height = 3 still

# sample_buildings[4] = 3
# 3 = 3, so don't add to answer array
# answers = [7, 6]
# max_height = 3 still

# sample_buildings[3] = 4
# 4 > 3, so add to answer array
# answers = [7, 6, 3]
# max_height = 4 now

# sample_buildings[2] = 4
# 4 = 4, so don't add to answer array
# answers = [7, 6, 3]
# max_height = 4 still

# sample_buildings[1] = 5
# 5 > 4, so add to answer array
# answers = [7, 6, 3, 1]
# max_height = 5 now

# sample_buildings[0] = 3
# 5 > 3, so don't add to answer array
# answers = [7, 6, 3, 1]
# max_height = 5 still

# answers = [7, 6, 3, 1], should be in ascending order so will just have to sort this and return it which is an
# O(n) operation just like all our other activities. So still rounds out to O(n) time and O(n) space due to possible
# size of return array being the same size as input array.

# Implementation:
def sunset_views_no_stack(buildings, direction):
    answers = []

    start = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    index = start
    max_height = 0
    while 0 <= index < len(buildings):
        current_height = buildings[index]

        if current_height > max_height:
            answers.append(index)

        max_height = max(current_height, max_height)

        index += step

    if direction == "EAST":
        return answers[::-1]

    return answers


print(sunset_views_no_stack(sample_buildings, sample_direction))
print(sunset_views_no_stack(sample_buildings2, sample_direction2))

# Explanation: Stack version

# For the answer that utilizes a stack
