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

# In depth breakdown of above using example sample trees
# tree1 isn't empty so bypass that check
# tree1_stack = [tree1]
# tree2_stack = [tree2]

# Enter while loop cause length of tree1_stack isn't empty
# tree1_node = tree1_stack.pop() = 1
# tree2_node = tree2_stack.pop() = 1
# tree2_node = 1, not null so skip if check
# tree1_node.value += tree2_node.value = 1 + 1 = 2
# tree1_node.left exists so go to else statement
# tree1_stack.append(tree1_node.left) --> tree1_stack.append(3), tree1_stack = [3]
# tree2_stack.append(tree2_node.left) --> tree2_stack.append(5), tree2_stack = [5]
#