from tkinter import *
# Question

# Write a function that takes in a non-negative integer "k" and a "k-sorted" array of integers and returns the sorted
# version of the array. The solution must sort the array with a time complexity faster than O(n(log(n)) time.

# Notes:
# Can either sort array in place or return new sorted array
# A k-sorted array is an array where the elements are, at most, "k" positions away from their sorted positions.

# Example:
example_k_array = [3, 2, 1, 5, 4, 7, 6, 5]
example_k = 3

# The array is a k array because at most, any given element in the array is at worst 3 positions away from where they
# should be. IE: The 3 in the example is 2 positions away from its proper place, the 2 is in the right place or 0
# positions from where it should be, etc.

# Answer
# [1, 2, 3, 4, 5, 5, 6, 7]


# Optimal Space & Time Complexity:
# O(n(log(k)) time
# O(k) space
# n = number of elements in the array
# k = distance of elements from their correct positions


# Explanation:
# The first thing to take not of is the importance of "k". When trying to conceptually grasp the question and figure out
# where each element's proper location would be, at most you'll only ever have to compare k + 1 elements. This is
# because k represents the maximum distance any element might be from their proper position. IE:

# array = [3, 2, 1, 5, 4, 7, 6, 5]
# k = 3
# current_element = 3
# possible positions = [3, 2, 1, 5,(cutoff here) 4, 7, 6, 5]
# Since 3 is at most k (3) positions away from its proper position, at most we'll only have to compare up until the
# 3rd position/5. This is because 3 positions from 3/the 0th position is the 3rd position/5. It can't possibly be any
# other position beyond that point, so we only have to compare positions up until then. All that would need to be done
# now is to choose the minimum element and swap positions.


# This idea continues when you move onto further elements, however it becomes even more optimized since by then the
# previous elements should already be sorted, IE:
# array = [3, 2, 1, 5, 4, 7, 6, 5]
# k = 3
# current_element = 2
# possible positions = [3, 2, 1, 5, 4,(cutoff here) 7, 6, 5]
# By this point the element that comes before 2, the 0th position element, should already be sorted. Meaning will still
# only have to consider k+1 elements, previous elements can be ignored as they should already be sorted.


# Completed process:
# array = [3, 2, 1, 5, 4, 7, 6, 5]
# k = 3
# current_position = 0
# array[0] = 3
# possible positions = [3, 2, 1, 5,(cutoff here) 4, 7, 6, 5]
# Minimum element is array[2] = 1
# array = [1, 2, 3, 5, 4, 7, 6, 5]

# current_position = 1
# array[1] = 2
# possible positions = [1,(start here) 2, 3, 5, 4,(cutoff here) 7, 6, 5]
# Minimum element is array[1] = 1, already in place
# array = [1, 2, 3, 5, 4, 7, 6, 5]

# current_position = 2
# array[2] = 3
# possible positions = [1, 2,(start here) 3, 5, 4, 7,(cutoff here) 6, 5]
# Minimum element is array[2] = 3, already in place
# array = [1, 2, 3, 5, 4, 7, 6, 5]

# current_position = 3
# array[3] = 5
# possible positions = [1, 2, 3,(start here) 5, 4, 7, 6(cutoff here), 5]
# Minimum element is array[4] = 4, swap
# array = [1, 2, 3, 4, 5, 7, 6, 5]

# current_position = 4
# array[4] = 5
# possible positions = [1, 2, 3, 4,(start here) 5, 7, 6, 5(cutoff here)]
# ********************Special case**********************************************************************
# Minimum element is array[4] = 5 or array[7] = 5, both same value so makes no difference if swap or not
# ********************Special case**********************************************************************
# array = [1, 2, 3, 4, 5, 7, 6, 5]

# current_position = 5
# array[5] = 7
# ********************Special case**********************************************************************
# Cutoff point is now outside array, meaning whatever elements are left are all that's left to sort so can just
# place them in ascending order.
# possible positions = [1, 2, 3, 4, 5, (start here)7, 6, 5](cutoff here)
# ********************Special case**********************************************************************
# Minimum element is array[7] = 5, swap
# array = [1, 2, 3, 4, 5, 5, 6, 7]

# current_position = 6
# array[6] = 6
# Notice already in place so continue

# current_position = 7
# array[7] = 7
# Notice already in place so done now

# Could also be done by creating a new array instead of just swapping elements, would just need to keep track of
# which elements have already been used somehow.


# How to implement optimally?:
# Despite what was shown, looking through k + 1 elements each time at each index wouldn't be optimal due to how many
# of the same elements would be repeatedly looked at/overlap. IE:
# array = [3, 2, 1, 5, 4, 7, 6, 5]
#          --------->
#             ---------->
#                --------->
#                    --------->
#                      --------->
#                         --------->
#                            --------->


# Lot of overlap pretty much, this can be avoided however with a Min-heap implementation.
# This is due to a Min-heaps property of always having its children nodes be greater than or equal to its parent node,
# meaning it would have a min-max tree like structure. With the root element being the smallest element.

# Time complexities to keep in mind for min-heap

# Get root element and or peek at it
# O(1) time

# Remove root/node
# O(log(n))
# n = number of heap elements, cause have to restore element after removing it

# Add element to heat
# O(log(n)) time

# Initialize heap
# O(n) time

# While a heap has more operations it can perform, this is all that will be needed for the optimal solution

# Code breakdown:
# Will need a few things to start out, first since going to sort in place a variable to keep track of which index
# has already been sorted alongside a heap that will be initialized to the current k+1 number of elements. IE:

# array = [3, 2, 1, 5, 4, 7, 6, 5]
# current_index = 0
# heap =                1 ---> 2
#          5 <--- 3 <--
# ********************Special case**********************************************************************
# Will need to watch out for edge cases where k > size of array
# ********************Special case**********************************************************************

# Use some sort of loop to begin looping at k + 1 elements, IE:
# 3 + 1 = 4, array[4] = 4
#

# Now place the top of the heap at the current index, 0. Will know it's where it belongs because it's the minimum of
# the current k + 1 elements.
# heap_root = 1,
# array = [1, 2, 1, 5, 4, 7, 6, 5]
# Adjust heap
# heap =  5 <--- 3 <-- 2
# Update index
# current_index = 1
# Add current loop position element to array,
# array[4] = 4
# heap =  4 <--- 3 <--- 2 ---> 5
# Done with first loop

# Repeat
# Update for loop to continue onto next element,
# [1, 2, 1, 5, 4, 7(loop here), 6, 5]
# current_index = 1
# heap =  4 <--- 3 <--- 2(root) ---> 5
# Add heap root to index position
# array = [1, 2, 1, 5, 4, 7, 6, 5]
# Update heap by changing root
# heap =  4 <--- 3(root) ---> 5
# Update index
# current_index = 2
# Add current loop position element to array,
# array[5] = 7
# heap = 7 <--- 4 <--- 3(root) ---> 5

# Update for loop to continue onto next element,
# [1, 2, 1, 5, 4, 7, 6(loop here), 5]
# current_index = 2
# heap = 7 <--- 4 <--- 3(root) ---> 5
# Add heap root to index position
# array = [1, 2, 3, 5, 4, 7, 6, 5]
# Update heap by changing root
# heap = 7 <--- 4 (root) ---> 5
# Update index
# current_index = 3
# Add current loop position element to array,
# array[6] = 6
# heap = 7 <--- 6 <--- 4 (root) ---> 5

# Update for loop to continue onto next element,
# [1, 2, 3, 5, 4, 7, 6, 5(loop here)]
# current_index = 3
# heap = 7 <--- 6 <--- 4 (root) ---> 5
# Add heap root to index position
# array = [1, 2, 3, 4, 4, 7, 6, 5]
# Update heap by changing root
# heap = 6 <--- 5 (root) ---> 7
# Update index
# current_index = 4
# Add current loop position element to array,
# array[7] = 5
# heap = 6 <--- 5 <--- 5(root) ---> 7

# Update for loop to continue onto next element,
# ********************Special case**********************************************************************
# [1, 2, 3, 4, 4, 7, 6, 5](loop here) Is outside of array, so no longer need to add any elements to the heap. Can just
# add heap elements into the current index position.
# ********************Special case**********************************************************************
# current_index = 4
# heap = 6 <--- 5 <--- 5(root) ---> 7
# Add heap root to index position
# array = [1, 2, 3, 4, 5, 7, 6, 5]
# Update heap by changing root
# heap = 6 <--- 5 (root) ---> 7
# Update index
# current_index = 5

# current_index = 5
# array = [1, 2, 3, 4, 5, 7, 6, 5]
# heap = 6 <--- 5 (root) ---> 7
# Add heap root to current index
# array = [1, 2, 3, 4, 5, 5, 6, 5]
# Update heap
# heap = 6(root) ---> 7
# Update index
# current_index = 6

# current_index = 6
# array = [1, 2, 3, 4, 5, 5, 6, 5]
# heap = 6(root) ---> 7
# Add heap root to current index
# array = [1, 2, 3, 4, 5, 5, 6, 5]
# Update heap,
# heap = 7 (root)
# Update index
# current_index = 7

# current_index = 7
# array = [1, 2, 3, 4, 5, 5, 6, 5]
# heap = 7 (root)
# Add heap root to current index
# array = [1, 2, 3, 4, 5, 5, 6, 7]
# Update heap
# heap = None/null

# Finished


# Time Complexity breakdown:

# Space
# O(k)
# Since sorting in place only extra space used is in heap, which at most will have k + 1 elements which can be reduced
# to k.

# Time
# O(n(log(k))
# n = number of elements in array

# n is from looping through input array at least once

# log(k) from removing from heap at each element since at most only ever k+1 elements in heap that reduces to k
# log(k) from adding element to heap at each element
# Can be seen as doing 2(log(k)) operations at each n that reduces to just log(k)

# k from initializing heap, but can be reduced from overall complexity due to how k is always less than or equal to n.
# This wouldn't change anything because of how the heap would still at most be n (all of them) elements.
# Meaning there could be a chance for k to be equal to n, that would transform possible time complexity to
# O(n(log(k)) + k) ---> O(n(log(k)) + n) ---> O(n(log(k)) + 1) ---> O(n(log(k))


# Implementation:
import heapq


def sortKSortedArray(array, k):
    idx_to_sort = 0

    # Because passed in k value could be equal to the size of the array, resulting in it going out of bound with
    # k + 1, a heap is made from the array stretching from whichever is smaller. k + 1 or the length of the array.
    # This is really more the size of the heap being made than the heap itself, however.
    heap = array[: min(k + 1, len(array))]

    # Transform the heap variable into an actual heap, happens in linear time
    heapq.heapify(heap)

    # For loop to go from the start of k + 1 in the array till the end
    for idx in range(k + 1, len(array)):
        # Set the index to sort in the array to be equal to the top of the heap/root.
        array[idx_to_sort] = heapq.heappop(heap)
        # Increment the index to sort by 1
        idx_to_sort += 1
        # Add the current k + 1 element to the heap
        heapq.heappush(heap, array[idx])

    # Once finished with the for loop, means have reached the end of the array and whatever elements are left
    # in the heap can just be placed in order in the array. Will continue until heap is emptied of elements.
    while len(heap) > 0:
        # # Set the index to sort in the array to be equal to the top of the heap/root.
        array[idx_to_sort] = heapq.heappop(heap)
        # Increment the index to sort by 1
        idx_to_sort += 1

    return array


print(sortKSortedArray(example_k_array, example_k))

# Visual of heap at each iteration
window = Tk()
example_image = PhotoImage(file='k_sort_array_visual.png')
example_label = Label(image=example_image)
example_label.pack()
window.mainloop()
