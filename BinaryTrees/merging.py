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
print(sample_tree1.value)



# Optimal Space & Time Complexity:
# O(n) time - because at the minimum will have to iterate through every node of the smaller tree
# O(h) space - because will either take up enough calls on the call stack equivalent to the 
# n = number of nodes in smaller of trees
# h = height of shorter tree

















# Implementation:
# Note: Both solutions focus on mutating tree1 and returning it but could easily be interchanged to tree2 being
# the mutated returned tree.
def merge_recursive(tree1, tree2):
    # If the node in the first tree doesn't exist, just return whatever node/branch tree2 is on
    if tree1 is None:
        return tree2
    # Same idea here, but for tree 2. If the node in tree2 doesn't exist, just return whatever node/branch tree1 is on
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


# Another solution, just iteratively. Runs in same time and space.
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

        # Case where non mutated tree could have a nonexistent node, simply continue
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
            # If doesn't exist just set its value to be the equivalent node of the right tree
            tree1_node.right = tree2_node.right
        # Else append both tree's right nodes to the top of their respective stacks
        else:
            tree1_stack.append(tree1_node.right)
            tree2_stack.append(tree2_node.right)

    # Return mutated tree1
    return tree1
