# Question
# Given two binary trees, merge them and return the resulting tree. Any overlapping nodes should be summed and returned
# as such in the resulting tree, else use whatever existing node(s) are already there.

# Note:
# Returning tree can either mutate existing tree or create new one


# Example:























# Implementation:
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def merge(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = merge(tree1.left, tree2.left)
    tree1.right = merge(tree1.right, tree2.right)
    return tree1
