# Question:

# Write a function that takes in a BT and inverts it. IE: The funtion should swap every left node in the tree
# for it's corresponding right node. 


# Example:
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Tree =   1
#         2   3
#      4 5    6 7
#    8 9
#

# Visual example at end of program
example_tree = BinaryTree(-1)
# Right side of tree
example_tree.right = BinaryTree(3)
example_tree.right.left = BinaryTree(6)
example_tree.right.right = BinaryTree(7)

# Left side of tree
example_tree.left = BinaryTree(2)
example_tree.left.right = BinaryTree(5)
example_tree.left.left = BinaryTree(4)
example_tree.left.left.left = BinaryTree(8)
example_tree.left.left.right = BinaryTree(9)




# Result:
#       1
#     3   2
#  7  8   5  4
#            9 8

# Notes:
# An inverted Binary Tree is symetrical 


# Optimal Space & Time Complexity:
# O (n) time, n = number of nodes in BT
# O (d) space, d = depth (height) of BT. (Note: d could also be log(n) instead since BT depths are essentially that.)


# Explanation:
# The biggest thing to realize for this problem is that recursion will be what works most efficiently due to the nature of how
# BTs can be traversed. Either BFS or DFS would work but the main idea would be to make recursive calls to invert each side.
# Doing so would result in the longest call in the call stack being equal to the depth of the BT, which would explain the space
# complexity being O(d). For the time complexity it's O(n) due to having to at some point traverse each and every node.

# Optimal Solution:










# Bonus most optimal and clean solution:
def invertBT(tree):
    if tree is None:
            return
    else:
         invertBT(tree.left)
         invertBT(tree.right)
         tree.left, tree.right = tree.right, tree.left





# Bonus unoptimal solution









