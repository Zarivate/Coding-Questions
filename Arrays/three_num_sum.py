# Question:
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in array that sum up to target and return a two-dimensional array of these
# triplets.

# Note:
# Both the numbers in each triplet and triplets themselves should be ordered in ascending order with respect
# to the numbers they hold.

# Example:
array_sample = [12, 3, 1, 2, -6, 5, -8, 6]
target_sample = 0

# Answer:
# [ [-8, 2, 6], [-8, 3, 5], [-6, 1, 5] ]

# Optimal Space Time Complexity:
# O(n^2) time
# O(n) space
# n = length of input array

# Explanation:
# The main idea involves first sorting the array, then traversing the array with 2 additional pointers for a total of 3
# numbers being tracked all at once. 1 pointer right after the current position, and the 2nd pointer at the last
# position. At each point, would check to see if all 3 numbers add up to target, if not then move pointers accordingly
# to target. IE, because the array would be sorted, depending on which end has the greatest values, we would only have
# to move the pointers on one of the sorted arrays side.

# Note:
# Sorting the array is an O(n(log(n)) operation but going through the loops in the while loop would be O(n^2)
# which dwarfs it and cause time complexity to be O(n^2)

# Implementation:

def three_num_sum(array, targetSum):
    # Sort array first
    array.sort()
    # Create an array to hold answers
    trips = []
    # For loop to iterate through array, will go until the second to last position in array because our right
    # pointer will go until the last position. So it would be redundant to go to the last one here.
    for i in range(len(array) - 2):
        # Set the left pointer to start 1 ahead of the outer for loop
        left_pointer = i + 1
        # Set the right pointer to the end of the array
        right_pointer = len(array) - 1
        # While loop to find all combinations for the value/position of "i"/the outer for loop. Will alter the
        # positions of the left and right pointers until left pointer overtakes right pointer position, because
        # by then all possible combinations will have been done
        while left_pointer < right_pointer:
            # Add up all the values
            current_sum = array[i] + array[left_pointer] + array[right_pointer]
            # Check if match target value
            if current_sum == targetSum:
                # If so add to answers array
                trips.append([array[i], array[left_pointer], array[right_pointer]])
                # Iterate left pointer by 1, ie: move forward in array by 1
                left_pointer += 1
                # Decrement right pointer by 1, ie: move backwards in array by 1
                right_pointer -= 1
            # If current total is less than the target, that means we need a greater value. Because the array is
            # sorted, we know that means we have to move the left pointer only.
            elif current_sum < targetSum:
                # Iterate left pointer by 1, ie: move forward in array by 1
                left_pointer += 1
            # If current total is greater than the target, that means we need a smaller value. Because the array is
            # sorted, we know that means we have to move the right pointer only.
            elif current_sum > targetSum:
                # Decrement right pointer by 1, ie: move backwards in array by 1
                right_pointer -= 1
    return trips


print(three_num_sum(array_sample, target_sample))