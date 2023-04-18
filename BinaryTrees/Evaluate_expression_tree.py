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

