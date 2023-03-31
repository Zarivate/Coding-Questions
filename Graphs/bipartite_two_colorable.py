from tkinter import *

# Note: Hadn't ever heard of the word "bipartite" until this question, still have lots to learn

# Question:
# Given a list of edges representing a graph with at least 1 node, write a function that returns True or False on
# whether that graph is two-colorable/bipartite if every node can have 1 of 2 colors and has no edge connecting
# any node of the same color.

# Notes:
# Graph is connected
# Graph is unweighted, no distance value between nodes
# Graph is undirected, meaning a node can go back and forth between any nodes it's connected to and vice versa.
# There is no 1 way nodes essentially.
# Graph may have self loops, meaning nodes that are connected to themselves forming a loop, if there are any self loops
# in the graphs then it's automatically not two-colorable/returns False
# Nodes and vertices are used interchangeably but refer to the same thing

# Example:

# edges = [
#   [1,3],
#   [0,2],
#   [1,3],
#   [0,2]
#        ] ]

# Answer:
# True


# Graph would look something like this
window = Tk()
example_image = PhotoImage(file='two_colorable_example.png')
example_label = Label(image=example_image, height=600)
example_label.pack()
window.mainloop()


# Explanation:
# What you'll need for this solution is some sort of data structure to keep track of a nodes colors and the
# current node we're at. For this an array consisting of the edges can be used while a stack can be
# used to determine which node to visit next, could be done in either BFS or DFS style.

# Since only need 2 colors for problem, can either designate a color variable string, IE: something like "red"
# or "blue" to be held in the array for each node or just simple "True/T" and "False/F". While the stack can
# start at any random node or the first one. Whichever node is chosen as the start for the stack, the stack will be
# updated to have the nodes/vertices that current node has edges to, IE: If we start at the 0 node our stack would
# go from
# stack = [0] = [1, 3], since node 0 has edges connecting to nodes 1 and 3

# Now in the array we made that holds the colors of the nodes, we update the colors. First of the node we're currently
# at, so we would have
# colors = [ T, _, _, _]
# Then it would go to
# colors = [ T, F, _, F], because nodes 1 and 3 need to be the opposite of node 0

# This process repeats until either find a connection that has the same color/or until reach end of array.

# **********************************
# Now pop the top node off the stack and look at its connections
# **********************************

# stack = [1, 3] = [3], after popping off 1

# **********************************
# edges[1] = [0,2], add only 2 to the stack because 0 already has a color, so we know it's already been visited/was in
# the stack. 2 doesn't have a color, so we know it's the first time we found that node.
# **********************************

# stack = [2, 3]
# Look at the edges/connections and assign colors if not already assigned
# 1 already has a color of "F", so it's connections should have "T", is this possible?
# colors = [ T, F, T, F], yes. 0 already has T and node 2 can be assigned T without running into any conflicts

# Keep going
# Pop the top node off the stack and look at its connections
# stack = [2, 3] = [3], after popping off 2
# edges[2] = [1,3], add neither to stack because they already have a color so we know they've been in the stack at some
# point
# stack = [3]
# Look at the edges/connections and assign colors if not already assigned
# 2 already has a color of "t", so it's connections should have "F", is this possible?
# colors = [ T, F, T, F], yes. 1 and 3 both already have "F"

# Keep going, pop 3 off the top of stack.
# stack = [3] = []
# Look at it's connections, and it's current color, if any
# edges[3] = [0, 2]
# colors = [T, F, T, F]
# Node 3 currently has "F", meaning nodes 0 and 2 must have "T". Which they do, now reached end of stack without
# running into any False cases so can return True


# Optimal Space & Time Complexity:
# O(v + e) time
# (Because of DFS approach and how are visiting each node and all their edges)

# O(v) space
# (Because creating extra space to store the array and stack, the array we make will always be of size
# v/size of the input array while the worst case scenario for the stack would be V as well since all the nodes
# could be connected and make a stack that has all the nodes at once. In which case we would have 2V, which rounds
# down to just V since constants aren't considered in Big O notation)

# v = number of vertices/nodes
# e = number of edges in graph


# Implementation:
def two_colorable(edges):
    colors = [None for _ in edges]
    # Set the first position/nodes color to be "True/T"
    colors[0] = True
    # Set the stack to start at the first node, which will have that node's edges
    stack = [0]

    # Continue until there is nothing left in the stack
    while len(stack) > 0:
        # Pop the node at the top of the stack
        node = stack.pop()
        # Look at the connections/edges the current node has
        for connection in edges[node]:
            # If the color of the current node being connected to is None/isn't assigned one in our colors array
            if colors[connection] is None:
                # Assign it the opposite color of the current node it has a connection to
                colors[connection] = not colors[node]
                # Add the connected node to the stack
                stack.append(connection)
            # If it finds a case where both the connected node and the node making the connection have the same
            # color, return False
            elif colors[connection] == colors[node]:
                return False
    return True


sample_edges = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(two_colorable(sample_edges))
