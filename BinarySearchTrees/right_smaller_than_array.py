from tkinter import *

# Question: (This one sucked by the way, would have never finished this one optimally without tips)

# Write a function that takes in an array of integers and returns an array of the same length where its
# indices correspond to the number of integers to the right of it in the original array that are strictly smaller
# than the original value in that position in the original input array.

# Example:

example_array = [8, 5, 11, -1, 3, 4, 2]
# This excludes the last value (2), since that was already used as a node before this point
for i in reversed(range((len(example_array) - 1))):
    print(example_array[i])


# Answer
# [5, 4, 4, 0, 1, 1, 0]
# 5 because in the original array, there are 5 values to the right of 8 that are smaller than it
# 4 because in the original array, there are 4 values to the right of 5 that are smaller than it
# 4 because in the original array, there are 4 values to the right of 11 that are smaller than it
# 0 because in the original array, there are 0 values to the right of -1 that are smaller than it
# 1 because in the original array, there is 1 value to the right of 3 that are smaller than it
# 1 because in the original array, there is 1 value to the right of 4 that are smaller than it
# 0 because in the original array, there are 0 values to the right of 2 that are smaller than it


# Optimal Space & Time Complexity:
# On Average when created BST is balanced
# O(n(log(n)) time
# O(n) space

# On Worst case when created BST looks like a linked list/one straight line down
# O(n^2) time
# O(n) space


# Explanation:
# To begin, it's best to first start at the most obvious, un-optimal solution and work our way to a more optimal one.
# The most obvious solution would be to use 2 pointers, 1 at the current node and then another to iterate through the
# rest of the array, keeping track of how many values are greater than the one the first pointer is at. These values
# would then be added to some sort of array and returned as an answer. A nested for loop pretty much. One that would
# result in

# O(n^2) time from having to iterate through at most n elements at each value,
# O(n) space from the size of the return array.

# Using this un-optimal solution, we can break down to see if it's possible to make it more optimal. First, see if the
# space can be made more optimal. This can quickly be seen to not be possible given how the answer requires an array
# of the same size to be returned. Meaning the space is already as optimal as it can be.

# Next, see if the time can be made more optimal beginning with the best possible and working towards a worse
# complexity.

# Is linear O(n) time possible?
# Unlikely, due to how the question is structured something like a linear time complexity wouldn't be feasible. This is
# because in order to know the answer to the corresponding position in the answer array, would need to iterate through
# the rest of the array. Something fancy with pointers wouldn't really work that well either since would need to have
# the array be sorted or have it contain some sort of extra information that could be used. Can't sort the array either
# since the result array depends on the current positions of the values in the input array.


# Is O(n(log(n) time possible?
# Since O(n^2) seems un-optimal, and O(n) seems impossible, this is the only possible one left. Now would be when
# algorithmic approaches and or data structures that run in log(n) or n(log(n) time could be considered. Beginning with

# Sorting algorithms, on average many run at O(n(log(n)) time but could all be immediately disregarded because of how,
# already stated before, sorting the array would change the answer array since the answer array depends on the current
# position of the values in the input array. Next would move onto

# Data structures,
# Given how we're looking for something with a time complexity that is worse than O(n) but better than O(n^2), only
# Binary Search Trees have time complexities that would fit as they have access, searching, insertion, and deletion
# time complexities of O(log(n)) on average. Given the nature of BSTs and how one of their properties correspond to
# how great or large the values must be, IE: all values to left of root node must be less than it while all values to
# right must be greater or equal to it, can use this to construct a BST that on average would meet our optimal time
# complexity.


# How would you insert the values though?
# It would be best to insert them from right to left. This is because of how the question wants to know how many values
# to the right of the specific index value are less than it, meaning if we insert them from right to left, as soon as
# they are inserted the answer for that specific index will be known. IE:

# example_array = [8, 5, 11, -1, 3, 4, 2]
# node = 2
# tree = 2
# there are 0 values less than it so can add that to the answer array [0]
# node = 4
# 4 > 2, so goes to the right of 2
# tree = 2 --> 4
# There is 1 value that is less than 4 so can add that to answer array [1, 0]
# node = 3
# 3 > 2, goes to right of 2
# 3 < 4, goes to left of 4
# tree =
# 2 --> 4
# 3 <-- 4
# There is 1 value less than 3 so can add that to answer array [1, 1, 0], etc

# *****************************************************************************************************************
# All the node insertions would be O(log(n)) and, so long as BST isn't unbalanced, on average would result in an
# O(n(log(n)) time complexity.
# *****************************************************************************************************************


# *****************************************************************************************************************
# You won't be able to get the correct answer for the result array once the BST is finished since that would change how
# many values are currently less than it so the problem comes when trying to actually keep track and store the correct
# values of how many integers are less than it in the tree so far.
# *****************************************************************************************************************

# This can be done by holding within the current node the size of it's left subtree, that way when nodes are inserted
# they can add the size of the left subtree of the node it is greater than alongside however many nodes it is greater
# than. This value would need to be updated as values are added though since future inserts may need this updated
# value to get the correct answer. IE

# node = 2
# tree = 2
# 2_left_side = 0
# current nodes 2 is greater than = 0
# 0 + 0 = 0, add 0 to answer array [0]

# node = 4
# 4 > 2, add to right of 2
# tree = 2 --> 4
# 2_left_side = 0
# 4_left_side = 0
# current nodes 4 is greater than = 1
# 1 + 0 = 1, add 1 to answer array [1, 0]

# *****************************************************************************************************************
# node = 3
# 3 > 2, add to right of 2
# 3 < 4, add to left of 4
# tree =
# 2 --> 4
# 3 <-- 4
# 2_left_side = 0
# 4_left_side = 1, the value goes from 0 to 1 now since 3 is now in 4's left subtree
# 3_left_side = 0
# current nodes 3 is greater than = 1
# 1 + 0 = 1, add 1 to answer array [1, 1, 0]

# node = -1
# -1 < 2, add to left of 2
# tree =
# -1 <-- 2 --> 4
# 3 <-- 4
# 2_left_side = 1, the value goes from 0 to 1 now since -1 is now in 2's left subtree
# 4_left_side = 1,
# 3_left_side = 0
# -1_left_side = 0
# Current nodes -1 is greater than = 0
# 0 + 0 = 0, add 0 to answer array [0, 1, 1, 0]

# node = 11
# 11 > 2, add to right of 2
# 11 > 4, add to right of 4
# tree =
# -1 <-- 2 -> 4
# 3 <-- 4 --> 11
# 2_left_side = 1, the value goes from 0 to 1 now since -1 is now in 2's left subtree
# 4_left_side = 1,
# 3_left_side = 0
# -1_left_side = 0
# 11_left_side = 0
# *****************************************************************************************************************
# Current nodes 11 is greater than = 4
# This is because 11 is greater than 2, 2 has a left subtree of 1. So would have 2 values greater than it right there.
# Then 11 is greater than 4, 4 has a left subtree of 1 so would have 2 values there as well.
# 2 + 2 = 4, add 4 to answer array [4, 0, 1, 1, 0]
# *****************************************************************************************************************
# Keep going until reach end

# In order to pass these values down to get the correct value in the answer array, recursion could be used.


# Implementation:
def rightSmallerThan(array):
    # Check for edge case where input array is empty
    if len(array) == 0:
        # If so just return an empty array
        return []

    # Duplicate the array to adjust the values for later
    answers = array[:]
    # Get the last index in the array
    last_idx = len(array) - 1
    # Create the BST using the last value in the array as the root node
    bst_root = BST(array[last_idx])
    answers[last_idx] = 0
    # This is an O(n) operation, to iterate through each value in the array
    for i in reversed(range(len(array) - 1)):
        # This is an O(log(n) operation at each node to insert, meaning would have an O(n(log(n) time complexity here
        bst_root.insert(array[i], i, answers)

    return answers


class BST:
    def __init__(self, value):
        self.value = value
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, answers, num_smaller_at_insert_time=0):
        if value < self.value:
            self.left_size += 1
            if self.left is None:
                self.left = BST(value)
                answers[idx] = num_smaller_at_insert_time
            else:
                self.left.insert(value, idx, answers, num_smaller_at_insert_time)
        else:
            num_smaller_at_insert_time += self.left_size
            if value > self.value:
                num_smaller_at_insert_time += 1
            if self.right is None:
                self.right = BST(value)
                answers[idx] = num_smaller_at_insert_time
            else:
                self.right.insert(value, idx, answers, num_smaller_at_insert_time)
