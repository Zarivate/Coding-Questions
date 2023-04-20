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
# O(h) space (Because the size of the call stack will be equivalent to the height of the tree. IE, the height of the
# call stack grows linearly with the size of the tree)
# n = number of nodes in Binary Tree
# h = height of Binary Tree


# Implementation:
def evaluate_tree(tree):
    # Base case are any positive integers, as all positive values are operands
    if tree.value >= 0:
        return tree.value

    # Set a variable to be equal to the left side value
    left_value = evaluate_tree(tree.left)
    # Set a variable to be equal to the right side value
    right_value = evaluate_tree(tree.right)

    # Check for which negative value tree is at and return the corresponding operation
    if tree.value == -1:
        return left_value + right_value
    if tree.value == -2:
        return left_value - right_value
    if tree.value == -3:
        return int(left_value / right_value)

    return left_value * right_value


print(evaluate_tree(example_tree))


# In depth breakdown:
# Most important thing to realize is how the entire problem is just a series of small operations, IE:
# Breakdown of tree from top to bottom would be like this
# result(left side) + result(right side)
# result(left_side) - 2, result(8/3)
# result(2*3)
# With each bottom result moving up to fill in the upper result, IE:
# result(left side) + (8/3), 8/3 is returned to the upper branch so now that will be added to the left side
# 6 - 2, 2*3 = 6 and is returned to the upper branch, so now we have 6-2
# Another call is finished
# 4 + (8/3), 8/3 rounded to 0 would be 2, so we would have 4 + 2 = 6
# Important thing is to just make sure the correct operation is being done when returning the result in the recursive
# call

# evaluate_tree(example_tree)
# tree.value = -4
# left_value = evaluate_tree(tree.left) = evaluate_tree(-2)
# right_value = evaluate_tree(tree.right) = evaluate_tree(-3)
# ***********************************************
# Now on evaluate_tree(-2) call
# tree.value = -2
# left_value = evaluate_tree(tree.left) = evaluate_tree(-4)
# right_value = evaluate_tree(tree.right) = evaluate_tree(2)
# ***********************************************
# Now on evaluate_tree(-4) call
# tree.value = -4
# left_value = evaluate_tree(tree.left) = evaluate_tree(2)
# right_value = evaluate_tree(tree.right) = evaluate_tree(3)
# ***********************************************
# Now on evaluate_tree(2) call
# 2 > 0, so return tree.value = 2
# evaluate_tree(2) = 2, tree.left = 2
# ***********************************************
# Now on evaluate_tree(3) call
# 3 > 0, so return tree.value = 3
# evaluate_tree(3) = 2, tree.right = 3
# ***********************************************
# Now can now move onto if check for -4,
# left_side * right_side
# 2 * 3 = 6
# ***********************************************
# Now can now move back up calls to left_value = evaluate_tree(tree.left) = evaluate_tree(-4) = 6
# left_value = 6
# finish right_value = evaluate_tree(tree.right) = evaluate_tree(2)
# right_value = 2
# ***********************************************
# Now back to evaluate_tree(-2)
# if check to see that tree.value = -2,
# left_value - right_value = 6 - 2 = 4
# left_side = evaluate_tree(-2) = 4
# ***********************************************
# Now back to evaluate_tree(-3)
# left_value = evaluate_tree(tree.left) = evaluate_tree(8)
# right_value = evaluate_tree(tree.right) = evaluate_tree(3)
# left_value = 8
# right_value = 3
# ***********************************************
# Now back again to evaluate_tree(-3)
# If check for -3 so operation is,
# left_side / right_side
# 8/3, remebering round to 0 rule would make it 2
# ***********************************************
# Finally back at top,
# tree.value = -1
# tree.left = 4
# tree.right = 2
# If check for -1 means operation is
# 4 + 2 = 6
# Return 6
