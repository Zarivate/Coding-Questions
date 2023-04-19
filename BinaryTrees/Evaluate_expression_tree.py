# Never even heard of this type of tree existing before this question by the way

# Question:
# Given a binary expression tree, write a function that evaluates the tree mathematically and returns a
# resulting integer.

# Notes:
# Can assume tree will always be a valid expression tree.
# All leaf nodes in the tree represent operands,
#       operands will always be positive integers
# All other nodes represent operators,
#       4 types of operators, each represented by a negative integer.
#       -1: Addition, add the left and right subtrees
#       -2: Subtraction, subtract right subtree from left subtree
#       -3: Division, divide left subtree by right subtree. If decimal result, round towards zero.
#       -4: Multiplication, multiply left and right subtrees
# Bottom of the tree always evaluated first, regardless of operator. This is because of how
# each operator also works as a grouping symbol

# Example:
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Visual example at end of program
example_tree = BinaryTree(-1)
example_tree.right = BinaryTree(-3)
example_tree.right.left = BinaryTree(8)
example_tree.right.right = BinaryTree(3)
example_tree.left = BinaryTree(-2)
example_tree.left.right = BinaryTree(2)
example_tree.left.left = BinaryTree(-4)
example_tree.left.left.left = BinaryTree(2)
example_tree.left.left.right = BinaryTree(3)


# Answer:
# 6 (Because (((2*3) - 2) + (8/3)) = 6 - 2 + 2  = 6)


# Optimal Space & Time Complexity:
# O(n) time
# O(h) space
# n = number of nodes in Binary Tree
# h = height of Binary Tree


# Implementation:
def evaluate_tree(tree):
    if tree.value >= 0:
        return tree.value

    left_value = evaluate_tree(tree.left)
    right_value = evaluate_tree(tree.right)

    if tree.value == -1:
        return left_value + right_value
    if tree.value == -2:
        return left_value - right_value
    if tree.value == -3:
        return int(left_value / right_value)

    return left_value * right_value


print(evaluate_tree(example_tree))


# In depth breakdown:
