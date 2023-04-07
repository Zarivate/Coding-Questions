from tkinter import *


# Question:
# Write a function that takes in a Binary Search Tree (BST) and a target integer and returns the closest value to
# the target integer within it.

# Note:
# Can assume there will only be 1 closest value
# Each BST has an integer value, a left child node, and a right child node
# A node is a valid BST node if and only if it satisfies the properties of BSTs
# 1. It's value (root) is greater than all left side nodes
# 2. It's value (root) is less than all right side nodes
# 3. Child nodes are either valid BST nodes too and or none/null

# Example:
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


sample_tree = BST(10)
sample_tree.left = BST(5)
sample_tree.left.right = BST(5)
sample_tree.left.left = BST(2)
sample_tree.left.left.left = BST(1)
sample_tree.right = BST(15)
sample_tree.right.right = BST(22)
sample_tree.right.left = BST(13)
sample_tree.right.left.right = BST(14)

# Would look something like this
window = Tk()
example_image = PhotoImage(file='closest_value_example.png')
example_label = Label(image=example_image)
example_label.pack()
window.mainloop()

target_sample = 12


# Answer:
# 13


# Optimal Space & Time Complexity:

# Average case:
# O(log(n)) time (On average won't go through entire tree to find answer)
# O(1) space
# n = number of nodes in BST

# Worst case:
# O(n) time (Because could be case where tree is just one long branch, which could result in having to go through
# the entire tree at worst)
# O(1) space

# Explanation:
# The main idea is to iterate through the tree once, however as you iterate you keep track of which value is the
# closest to the target integer. By comparing the absolute differences between the target value and the current node's
# value and the current closest value. If the absolute difference is greater with the current closest value than
# the absolute difference with the current node's value, that means the new closest value would be the new current
# node. After this can decide how to move through the array by seeing if the target value is greater than or less than
# the current node's value. Since it's a BST, can know to move left for smaller value nodes and right for greater
# value nodes.


# Implementation:
def closest_value_in_bst(tree, target):
    return find_closest_helper(tree, target, tree.value)


def find_closest_helper(tree, target, closest_value):
    # Set the current node to be equal to the current tree/node passed in
    current_node = tree
    # Loop to go until end of branch is found/node is null
    while current_node is not None:
        # Check to see if the absolute difference between the target and current closest value (at the start would be
        # the root value) is greater than the absolute difference between the target and current node's value. If so,
        # means the current node's value is closer to the target, so we update the closest value variable.
        if abs(target - closest_value) > abs(target - current_node.value):
            closest_value = current_node.value
        # Check to see if the target is less than the current node's value
        if target < current_node.value:
            # If so, move to the left side/branch of the tree
            current_node = current_node.left
        # Check to see if the target is greater than the current node's value
        elif target > current_node.value:
            # If so, move to the right side/branch of the tree
            current_node = current_node.right
        # If no conditions are met, can break out of loop
        else:
            break
    return closest_value

# In depth walkthrough:
# At start
# tree = 10, target = 12, closes_value = 10


print(closest_value_in_bst(sample_tree, target_sample))