# Question:

# Write a function that takes in an array of integers and returns a sorted version of that array using the Merge Sort
# algorithm. 

# Example:
example_array = [8, 5, 2, 9, 5, 6, 3]

# Answer:
# example_array = [2, 3, 5, 5, 6, 8, 9]

# Optimal Space & Time Complexity:
# Best, Worst, and Average Case:
# O(nlog(n)) time
# O(n) space 
# n = length of input array

# A simple function meant to print out the array to see if the answer is correct
def printOutArray(array):
    for value in array:
        print(value, end=" ")

# Explanation:
# To start, the unoptimal approach will be detailed out first. This approach involves doing nothing more than doing a simple merge 
# sort algorithm approach with no special adjustments. Split the array in half, creating new arrays, recursively repeat until arrays 
# are of size 1, then gradually create new sorted arrays from the split arrays until new final sorted array is completed, IE: 

# example_array = [8, 5, 2, 9, 5, 6, 3]
# length = 7
# 7/2 rounded down = 3
# Split at the 3 point to get

# left_array = [8, 5, 2, 9], right_array = [5, 6, 3]
# Split once more, beginning with left side as this would be recursive

# left_array = [8, 5, 2, 9]
# length = 4
# 4/2 = 2
# left_array = [8, 5], right_array = [2, 9]
# Split once more, beginning with left side again

# left_array = [8, 5]
# length = 2
# left_array = [8], right_array = [5]

# Arrays are now of size 1, so can go back up and sort them to get
# sorted_array = [5, 8]

# Move back up to right_array = [2, 9] and repeat process
# left_array = [2], right_array = [9]

# Arrays are now of size 1, so can go back up and sort them to get
# sorted_array = [2, 9]

# Now have two sorted arrays of [5, 8] and [2,9]. Repeat sorting process on these and create new array of
# sorted_array = [2, 5, 8, 9]

# Completely done with left side so can repeat process on remaining right side
# right_array = [5, 6, 3]
# length = 3
# 3/2 rounded down = 1

# left_array = [5, 6], right_array = [3]
# Right side is already just 1, but left side is not so repeat process on left side

# left_array = [5, 6]
# left_array = [5], right_array = [3]
# Combine back together and sort to get
# sorted_array = [5, 6]

# Compare new sorted array to remaining single length right array 
# sorted_array = [5, 6], right_array = [3]
# sorted_array = [3, 5, 6]

# Now have completed both halves, and have 2 arrays of 
# [2, 5, 8, 9] and [3, 5, 6]
# Combine these two into a new array and sort to get

# sorted_array = [2, 3, 5, 5, 6, 8, 9]

# This approach runs in 
# O(nlog(n)) space and time which is not ideal space wise, which is why the optimal approach is a bit trickier


# Optimal Explanation:
# This solution's main goal is to solve the problem in constant space which can be done using pointers. The tricky part is just keeping track of the pointers.
# The main idea however is similar to the previous method where it's done recursively, just that pointers are used now during each iteration to know where to
# IE:




# Implementation (Optimal)
def mergeSort(array):

    # Base case is still the same, where any array of size 1 is just returned
    if len(array) <= 1:
        return array


    # Find the middle point of the array
    middle = len(array) // 2
    # Make recursive calls to the mergeSort function on the two halves of the array
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])

    # Create an empty array that will hold the sorted answer
    sorted = []
    # Set two pointers, one for the left side and another for the right
    i = 0
    j = 0
    # So long as neither pointer reaches the end of either side of the array
    while i < len(left) and j < len(right):
        # If the value at the left position is less than the value at the right position
        if left[i] < right[j]:
            # Append the smaller value first, the left position value
            sorted.append(left[i])
            # Iterate the left side pointer by one
            i += 1
        # If that's not the case then it means the right value is smaller, so append that one instead and increment it's pointer
        else:
            sorted.append(right[j])
            j += 1

    # If the pointer reaches the end of it's side
    if i == len(left):
        # Set it's pointer to be equal to the right pointer
        i = j
        # Set the left array to be the same as the right
        left = right
    # While the end of the left(now right side) hasn't been reached yet
    while i < len(left):
        # Append the left position value to the array
        sorted.append(left[i])
        # Increment it
        i += 1

    return sorted

# Print out array before sorting
printOutArray(example_array)
print()
# Print out array after sorting
printOutArray(mergeSort(example_array))