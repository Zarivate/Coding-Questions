from tkinter import *
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

# Explanation: Stack version

# The main idea to keep in mind is that a Stack's LIFO/FILO property can be used to get the correct buildings. What's
# important to realize is that because buildings can only see the sunset if their heights are greater than all the ones
# following it, if you iterate in the proper direction the sun is pointing at, and add the buildings accordingly,
# you can compare the following building heights to the ones on the stack and keep popping off buildings until you only
# have ones with heights greater than or equal to the current building's height. Ensuring that the only buildings in
# the stack are those able to see the sunset. Though in the event that you need to start at the end of the array if
# pointing WEST, will need to reverse the array before returning the results. IE:

# sample_buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# sample_direction = "EAST"

# Initialize an empty stack that will hold the answers.
# answers = []
# Then just iterate through the array and compare the current buildings height with the max, are two possibilities.
# If you find that
# the current building has a height greater than or equal to the height of the building at the top of the stack,
# pop the top building off the stack and keep popping until find a building with a greater height or until stack
# is empty. After that, add it to the stack.
# If you find that
# the current building has a height less than the height of the building at the top of the stack, add to stack. Don't
# pop anything.

# In depth example:

# stack = []
# sample_buildings[0] = 3
# Top of stack is empty so can just add since 3 > 0
# stack = [0]
# sample_buildings[1] = 5
# 5 > 3, so pop 3 off stack and add 5
# stack = [1]
# sample_buildings[2] = 4
# 5 > 4, less than so add to stack.
# stack = [1, 2]
# sample_buildings[3] = 4
# 4 = 4, equal to so pop off stack,
# stack = [1]
# 5 > 4, less than so add to stack,
# stack = [1, 3]
# sample_buildings[4] = 3
# 4 > 3, less than so add to stack,
# stack = [1, 3, 4]
# sample_buildings[5] = 1
# 3 > 1, less than so add to stack,
# stack = [1, 3, 4, 5]
# sample_buildings[6] = 3
# 1 < 3, greater than top of stack so pop
# stack = [1, 3, 4]
# 3 = 3, equal to so pop off stack,
# stack = [1, 3]
# 4 > 3, less than so add to stack,
# stack = [1, 3, 6]
# sample_buildings[7] = 2
# 3 > 2, less than so add to stack,
# stack = [1, 3, 6, 7]
# Return stack, if direction is opposite one will just need to reverse stack which would be an O(n) operation

# Time Complexity breaks down like so:
# Time:
# O(n) to iterate through array
# O(n), in worst case will have to pop n elements off the stack each time
# O(n) again to reverse stack, if in opposite direction to get correct order of results

# Space:
# O(n), at most will only have n elements in stack

# Implementation:
def sunset_views_stack(buildings, direction):
    # Stack to hold answers
    answers = []

    # Depending on the direction, the starting index is adjusted
    index = 0 if direction == "EAST" else len(buildings) - 1
    # Depending on the direction again, the value to increment through the array with is different
    step = 1 if direction == "EAST" else -1

    # While loop to iterate through array
    while 0 <= index < len(buildings):
        # Set value to hold the current buildings height
        current_building_height = buildings[index]

        # While loop to continue so long as stack isn't empty and the height of the building at the top of the stack
        # is less than the current buildings height
        while len(answers) > 0 and buildings[answers[-1]] <= current_building_height:
            # Pop top value off stack
            answers.pop()

        # Add building index to stack
        answers.append(index)

        # Iterate through array
        index += step

    # If the direction is WEST, reverse the stack before returning it
    if direction == "WEST":
        return answers[::-1]

    return answers


print(sunset_views_stack(sample_buildings, sample_direction))
print(sunset_views_stack(sample_buildings2, sample_direction2))


# Bonus Explanation: Non-stack version
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
    # Set up an array to hold the return results
    answers = []

    # Set the starting index to either be at the start or end of the array depending on the direction
    index = 0 if direction == "WEST" else len(buildings) - 1
    # Value to decide whether to move forward or backwards in the array depending on the direction
    step = 1 if direction == "WEST" else -1

    # Max height variable to be compared to buildings later, set to 0 as no buildings with 0 or negative height
    max_height = 0
    # While loop to iterate through the array, either till end or start of array depending on direction
    while 0 <= index < len(buildings):
        # Set the current height to be equal to the current building height
        current_height = buildings[index]

        # Compare to max height, if greater, then add to answer array and set the max height to be equal to it
        if current_height > max_height:
            answers.append(index)
            max_height = current_height

        # Adjust the index in the array
        index += step

    # In the event that the direction is east and the answers are in reverse, simply reverse the array
    if direction == "EAST":
        return answers[::-1]

    # Return results
    return answers


print(sunset_views_no_stack(sample_buildings, sample_direction))
print(sunset_views_no_stack(sample_buildings2, sample_direction2))

# Visual example of problem
window = Tk()
example_image = PhotoImage(file='Stacks/sunset_views_example.png')
example_label = Label(image=example_image)
example_label.pack()
window.mainloop()