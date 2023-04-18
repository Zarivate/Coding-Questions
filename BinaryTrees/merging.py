from tkinter import *


# Question
# Given two binary trees, merge them and return the resulting tree. Any overlapping nodes should be summed and returned
# as such in the resulting tree, else use whatever existing node(s) are already there.

# Note:
# Returning tree can either mutate existing tree or create new one


# Example:
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Visual example at end of program
sample_tree1 = BinaryTree(1)
sample_tree1.right = BinaryTree(2)
sample_tree1.left = BinaryTree(3)
sample_tree1.left.left = BinaryTree(7)
sample_tree1.left.right = BinaryTree(4)

sample_tree2 = BinaryTree(1)
sample_tree2.right = BinaryTree(9)
sample_tree2.left = BinaryTree(5)
sample_tree2.left.left = BinaryTree(2)
sample_tree2.right.left = BinaryTree(7)
sample_tree2.right.right = BinaryTree(6)

# This is a duplicate of the first tree, here because of how both solutions don't create any new trees, instead
# they utilize the same trees and just mutate and return one as the answer. Because of this, the second solution uses
# the already mutated tree from the first solution, resulting in the wrong answer. To avoid this, a duplicate is made.
sample_tree3 = BinaryTree(1)
sample_tree3.right = BinaryTree(2)
sample_tree3.left = BinaryTree(3)
sample_tree3.left.left = BinaryTree(7)
sample_tree3.left.right = BinaryTree(4)


def print_tree_depth_first_search(tree):
    tree_stack = [tree]
    while len(tree_stack) > 0:
        tree_node = tree_stack.pop()
        print(tree_node.value)
        if tree_node.left is None:
            continue
        else:
            tree_stack.append(tree_node.left)
        if tree_node.right is None:
            continue
        else:
            tree_stack.append(tree_node.right)


print_tree_depth_first_search(sample_tree1)
print()
print_tree_depth_first_search(sample_tree2)
print()


# Optimal Space & Time Complexity:
# O(n) time - because at the minimum will have to iterate through every node of the smaller tree
# O(h) space - because will either take up enough calls on the call stack equivalent to the height of the smaller tree
# or an equivalent amount of space in the stacks for the iterative solution. (More in depth explanation below)
# n = number of nodes in smaller of trees
# h = height of shorter tree


# Implementation:
# Note: Both solutions focus on mutating tree1 and returning it but could easily be interchanged to tree2 being
# the mutated returned tree.
def merge_recursive(tree1, tree2):
    # Base case where if either tree is null/none, just return the other tree
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1
    # Increment the node value in the first tree by the corresponding node value in tree2
    tree1.value += tree2.value
    # Call the recursive function on both of the tree's left nodes
    tree1.left = merge_recursive(tree1.left, tree2.left)
    # Call the recursive function on both of the tree's right nodes
    tree1.right = merge_recursive(tree1.right, tree2.right)
    # Return mutated tree1
    return tree1


new_tree_recursive = merge_recursive(sample_tree1, sample_tree2)
print()
print_tree_depth_first_search(new_tree_recursive)


# In depth breakdown using sample trees 1 and 2
# merge_recursive(sample_tree1, sample_tree2)
# neither tree1 nor tree2 is None so skip if checks
# tree1.value += tree2.value = 1 + 1 = 2
# tree1.left = merge_recursive(tree1.left, tree2.left) = merge_recursive(3, 5)

# **************************************************
# Recursive call, neith tree1 or tree2 is None so skip if check
# tree1.value += tree2.value = 3 + 5 = 8
# tree1.left = merge_recursive(tree1.left, tree2.left) = merge_recursive(7, 2)

# **************************************************
# Recursive call, neith tree1 or tree2 is None so skip if check
# tree1.value += tree2.value = 7 + 2 = 9
# tree1.left = merge_recursive(tree1.left, tree2.left) = merge_recursive(None, None)

# **************************************************
# Both tree1 and tree2 are None so return tree2/leaf node already there as that would be the first if check,
# tree2 = None, returns an empty leaf node
# **************************************************
# Can now go back in call stack to tree1.left = merge_recursive(7, 2) = tree2 = None/empty leaf node, and move onto
# tree1.right = merge_recursive(tree1.right, tree2.right) = merge_recursive(None, None)
# Both tree1 and tree2 are None so return tree2/leaf node already there as that would be the first if check,
# tree2 = None, returns an empty leaf node
# tree1.right = tree2 = None
# Finally reached end of function, return tree1
# **************************************************
# Now go back in call stack at merge_recursive(5, 3) and move onto
# tree1.right = merge_recursive(tree1.right, tree2.right) = merge_recursive(4, None)
# tree1 is 4 but tree2 is None so return tree1.
# tree1.right = tree1 = 4
# **************************************************

# Go back in call stack at merge_recursive(1, 1), and move onto
# tree1.right = merge_recursive(tree1.right, tree2.right) = merge_recursive(2, 9)
# Neither tree1 nor tree2 are none so continue
# tree1.value += tree2.value = 2 + 9 = 11
# tree1.left = merge_recursive(tree1.left, tree2.left) = merge_recursive(None, 7)
# tree1 is None so return tree2
# tree1.left = merge_recursive(None, 7) = tree2 = 7

# **************************************************
# Go back in call stack at merge_recursive(2, 9), and move onto
# tree1.right = merge_recursive(tree1.right, tree2.right) = merge_recursive(None, 6)
# tree1 is None so return tree2
# tree1.right = merge_recursive(None, 6) = 6
# Can now return tree1 and finish

# Another solution, just iteratively. Runs in same time and space. Will know are finished when both stacks are empty.
# Utilizes Depth First Search(DFS).
def merge_iteratively(tree1, tree2):
    # Since iterative don't have to account for both trees, only the one being mutated. If the first tree's
    # node is empty, just return the second tree.
    if tree1 is None:
        return tree2

    # Set both trees to be a stack so node values can be popped off
    tree1_stack = [tree1]
    tree2_stack = [tree2]

    # So long as the first tree's stack isn't empty
    while len(tree1_stack) > 0:
        # Pop a node off both stacks
        tree1_node = tree1_stack.pop()
        tree2_node = tree2_stack.pop()

        # Case where non mutated tree could have a nonexistent node, simply continue in while loop.
        # No need to do any of the checks and increments at this node since would be adding nothing.
        if tree2_node is None:
            continue

        # Increment the node value in the first tree by the corresponding node value in tree2
        tree1_node.value += tree2_node.value

        # If check to see if the node in the first tree doesn't exist
        if tree1_node.left is None:
            # If so just set its value to be equivalent to the second tree's node value
            tree1_node.left = tree2_node.left
        # Else append both tree's left nodes to the top of their respective stacks
        else:
            tree1_stack.append(tree1_node.left)
            tree2_stack.append(tree2_node.left)

        # Same idea as above, but now for the right side of the tree. Check to see if it's right node exists.
        if tree1_node.right is None:
            # If it doesn't exist just set its value to be the equivalent node of the right tree
            tree1_node.right = tree2_node.right
        # Else append both tree's right nodes to the top of their respective stacks
        else:
            tree1_stack.append(tree1_node.right)
            tree2_stack.append(tree2_node.right)

    # Return mutated tree1
    return tree1


new_tree_iterative = merge_iteratively(sample_tree3, sample_tree2)
print()
print_tree_depth_first_search(new_tree_iterative)

# In depth breakdown of above using example sample trees
# tree1 isn't empty so bypass that check
# tree1_stack = [tree1] = [1]
# tree2_stack = [tree2] = [1]

# Enter while loop cause length of tree1_stack isn't empty
# tree1_node = tree1_stack.pop() = 1
# tree2_node = tree2_stack.pop() = 1
# tree2_node = 1, not null so skip if check
# tree1_node.value += tree2_node.value = 1 + 1 = 2
# tree1_node.left exists so go to else statement
# tree1_stack.append(tree1_node.left) --> tree1_stack.append(3), tree1_stack = [3]
# tree2_stack.append(tree2_node.left) --> tree2_stack.append(5), tree2_stack = [5]
# tree1_node.right = 2, is not None/null so go to else check
# tree1_stack.append(tree1_node.right) --> tree1_stack.append(2), tree1_stack = [2, 3]
# tree2_stack.append(tree2_node.right) --> tree2_stack.append(9), tree2_stack = [9, 5]
# **************************************************
# Go back to while loop,
# **************************************************

# tree1_node = tree1_stack.pop() = 2
# tree2_node = tree2_stack.pop() = 9
# tree2_node = 9, not null so skip if check
# tree1_node.value += tree2_node.value = 9 + 2 = 11
# **************************************************
# This effectively just takes the branch of the second tree and attaches it to the first tree
# tree1_node.left doesn't exist so go inside if check statement
# tree1_node.left = tree2_node.left = 7
# tree1_node.right doesn't exist so go inside if check statement
# tree1_node.right = tree2_node.right = 6
# **************************************************
# Go back to while loop, etc

# Visual example of problem alongside answer
window = Tk()
example_image = PhotoImage(file='Merge_binary_trees_example.png')
example_label = Label(image=example_image)
example_label.pack()
window.mainloop()
