# Question:

# Given an array of buildings and the direction they're facing, return an array of the indices of the buildings that
# can see the sunset.

# Notes:
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

# Optimal Space & Time Complexity:

