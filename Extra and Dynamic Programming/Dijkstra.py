import sys
import os
from dotenv import load_dotenv

load_dotenv()
resizePath = os.getenv("RESIZEPATH")

sys.path.insert(1, resizePath)
from resizeImg import *
# Question

# Given an adjacency list representing a graph that holds "edges" comprised of pairs of integers, and an integer "start" value. 
# Utilize Djikstra's algorithm to find the shortest paths to each vertice in the graph and returns them in an array. 
# Where the index of the array represents the shortest path to that designated index. If there is no path to the vertice/index, 
# -1 should be placed in it's position in the answer array.

# Notes:

# No self loops
# No negative weights/edges
# All edges are directed in 1 direction only
# Length of adjacency list=number of vertices in graph, IE: In example length of list is 6 with vertices 0-5

# Example:
start = 0

example_edges = [
    [[1, 7]], # This represents vertex 0, that has one outgoing edge to 1 with a weight of 7
    [[2, 6], [3, 20], [4, 3]], # This represents vertex 1 with 3 outgoing edges, an edge to 2 with a weight of 6, edge to 3 with weight of 20, and edge to 4 with weight of 3
    [[3, 14]], # This represents vertex 2, that has one outgoing edge to 3 with a weight of 14
    [[4, 2]], # This represents vertex 3, that has one outgoing edge to 4 with a weight of 2
    [],
    [],
]



# Answer
# [0, 7, 13, 27, 10, -1]


# Optimal Space & Time Complexity:
# O((v + e) * log(v)) time | O(v) space
# v = Number of vertices
# e = Number of edges


# Explanation:
# The main idea behind Dijkstra's algorithm is to use the knowledge of prior path distances to find the shortest paths to each destination.
# For this problem, it would work in this problem by going through each vertice, their respective outgoing eges (if any), the shortest
# distance found at each one, all while simultaneously updating them and keeping track of which vertices have already been visited.
# It sounds like a lot and it's because it is and it sucks to code it optimally without using built in classes, here is a detailed
# breakdown however.


# Some data structure to keep track of already visited nodes. This will be updated at the end after each node's edges. Have been accounted
# for. Will update the visited with the node that has the shortest path that has yet to be visited. This information can then be used
# to save time when trying to find the shortest paths later one. Another way to think of it is how the data structure will hold the nodes
# in order of shortest to longest paths to them. Becomes clearer in example, I swear. 

# visited = {}

# Another data structure to keep track of the current shortest found distances to each node. This will be updated and refered to
# throughout the algorithm.
# The first/"start" value can be 0 since don't have to do any traveling to get to it.
# While the rest of the values are infinity so when comparisons are done to see whether a found path is shorter or not,
# it can be properly compared without worrying for a default value being greater than a distance value.

# shortest_paths = [0, inf, inf, inf, inf, inf], 


# Then just go through each list/value in the adjacency list and keep track of the outgoing edges and their subsequent distances. IE:

# edges = [
# 0    [[1, 7]], 
# 1    [[2, 6], [3, 20], [4, 3]], 
# 2    [[3, 14]], 
# 3    [[4, 2]], 
# 4    [],
# 5    [],
# ]

# Start at node 0, has one outgoing edge to 1 with a weight/distance of 7

# Update visited and shortest paths
# visited = {0} -> {0, 1}. At the end of node 0's edges, the node with the shortest path that has yet to be visited would be 1.
# shortest_paths = [0, inf, inf, inf, inf, inf] -> [0, 7, inf, inf, inf, inf]

# Move on to node 1, as that's the next visited node. Has 3 outgoing edges, update each one. Start with the first edge, [2, 6]. Path to 2 from 1 with distance of 6.
# visited = {0, 1}
# ********************************
# shortest_paths = [0, 7, 13, inf, inf, inf]
# It's not just 13 because 6 + 7 = 13, but because the shortest path to the node before it was 7. Which is why it was used.    
# ********************************

# Go to the second edge, [3, 20]. Path to 3 from 1 with a distance of 20.
# visited = {0, 1}
# ********************************
# shortest_paths = [0, 7, 13, 27, inf, inf]
# Is 27 because to get to 3 from 1, have to first get from 0 to 1. The shortest path from 0 to 1 is 7, so 7 + 20 = 27
# ********************************

# Go to the third edge, [4, 3]. Path to 4 from 1 with a distance of 3.
# ********************************
# visited = {0, 1} -> {0, 1, 4}, Is 4 because it has yet to be visited and has the shortest path of 10.
# ********************************
# shortest_paths = [0, 7, 13, 27, 10, inf]
# Is 10 because of same logic from before. Shortest path to 1 is 7, so just add that along with the distance to 4 to get 7 + 3 = 10
# ********************************

# Now move onto node 4, as comes next in visited data structure. Has no outgoing edges so instead look to see which node has the shortest path to update visited.
# ********************************
# visited = {0, 1, 4} -> {0, 1, 4, 2}, Is node 2 with a distance of 13.
# shortest_paths = [0, 7, 13, 27, 10, inf]
# ********************************

# Now move onto node 2, has 1 outgoing edge of [3, 14]. Update the visited and shortest paths accordingly.
# visited = {0, 1, 4, 2} -> {0, 1, 4, 2, 3}, Is 3 because not yet visited and has shortest remaining path of 27.
# ********************************
# shortest_paths = [0, 7, 13, 27, 10, inf]
# Is still 27 because the shortest path to node 2 is 13. 13 + 14 = 27. At this point the algorithm would just ignore updating this
# in the shortest paths since has the same distance.
# ********************************

# ******************************************************************************
# Onto node 3, has 1 outgoing edge of [4, 2]. 
# visited = {0, 1, 4, 2, 3} -> {0, 1, 4, 2, 3, 5}, 5 still has a default value of "inf", meaning it was never reached by the other nodes.
# ******************************************************************************
# shortest_paths = [0, 7, 13, 27, 10, inf]
# Shortest path to 4 would remain 10, not only because shortest path to node 3 is 27. Which is already bigger than the current shortest
# path to 4 of 10. But because 4 has already been visited, meaning it's shortest path has already been found/it was visited before node 3
# so it already has a shorter path to it than 3, so don't have to bother calculating anything and can save time. This is where
# Djikstra's algorithm comes in handy.
# Note: if there were negative weights, wouldn't be able to stop here due to the possibility of an edge case where a negative distance
# could result in a shorter path.
# ******************************************************************************

# Algorithm by this point could be over, since the visited set is the same length as the given adjacency list and because
# a visited node with the default value was found. Any time that happens, it's shortest distance would be -1 because still
# having the default value means no path to that node was found. So just have to update that node's value in the shortest paths
# to -1 and return for the answer.

# shortest_paths = [0, 7, 13, 27, 10, -1]


# Implementation: (Unoptimal)
# O(v^2 + e) time | O(v) space
# This version of the answer utilizes an array to keep track of the current shortest distances, which would have to be searched entirely
# everytime the node with the shortest distance needed to be found to updated the visited data structure. This results in a time complexity
# of O(v^2 + e) time. V^2 from having to iterate through the entire array of length V each time at the end of every node, and the e from
# having to go over every edge, only once however.
def dijkstrasAlgorithm(start, edges):
    # Get the number of nodes/vertices
    numVertices = len(edges)

    # Create the data structure to hold and update the shortest paths to each node
    minDistances = [float("inf") for _ in range(numVertices)]
    # Set the starting node distance to be 0
    minDistances[start] = 0

    # Create set to hold the visited nodes
    visited = set()

    # Keep iterating until all the nodes have been visited. This is a time complexity of V,
    while len(visited) != numVertices:
        # Get the current node and it's current minimum distance. This is another time complexity of V, which is where the v^2 comes
        vertex, currMinDistance = getInfo(minDistances, visited)

        # If any node's current minimum distance is ever still infinity, can break out of loop
        if currMinDistance == float("inf"):
            break

        # Add the current node to the visited data structure
        visited.add(vertex)

        # Iterate through the current node's edges/outgoing paths
        for edge in edges[vertex]:

            # Grab the destination node and the path/weight to get to it
            node, path = edge

            # If the node has ever already been visited, can skip over it
            if node in visited:
                continue

            # Calculate the total distance to get to the destination node using the distance to the current node + the distance to the new one
            newDistance = currMinDistance + path
            # Grab the current minimum distance to the destination node
            currPathDistance = minDistances[node]
            # Compate the two, update accordingly
            if newDistance < currPathDistance:
                minDistances[node] = newDistance

    # Return a list of the shortest paths to each node, made easy with a lambda function.
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


# Function to get the following node to iterate through, IE: The unvisited node with the shortest distance
def getInfo(distances, visited):
    # Default values for comparison
    currMinDistance = float("inf")
    node = -1

    # This is where the v^2 would come into play, would have to iterate thorugh every value in the minDistances array at every node.
    for nodeIdx, distance in enumerate(distances):
        # If the node has already been visited, can skip it
        if nodeIdx in visited:
            continue
        # Else, check to see if the node's current Minimum distance is less than or equal to infinity,
        if distance <= currMinDistance:
            # If so then grab the node and set the current minimum distance to be the found distance
            node = nodeIdx
            currMinDistance = distance

    return node, currMinDistance
 
# Bonus: A short and quick rundown of getInfo using the first pass.

# This is the first call to getInfo from the outer while loop in the main function
# vertex, currMinDistance = getInfo(minDistances, visited)

# Breaks down like so
# getInfo(distances, visited)
# getInfo(minDistances[0, inf, inf, inf, inf, inf], {})

# currMinDistance = float("inf")
# node = -1

# Enter for loop
# nodeidx = 0, distance = 0
# 0 not in visited, so keep going in for loop
# 0 < infinity, so grab the nodeIdx as the node to be iterated over and return the shorter distance
# node = 0
# currMinDistance = 0
# return 0, 0

# vertex, currMinDistance = 0, 0

def printAnswer(array):
    for value in array:
        print(value, end=" ")


printAnswer(dijkstrasAlgorithm(start,example_edges))

# Visual example of problem
img_path = "Extra and Dynamic Programming\dijkstrasalgorithmexample.png"
imgResizeHalf(img_path, "Dijikstra's Algorithm Example")


# Optimal Solution: The optimal solution would only save time and would be done using a MinHeap. Would no longer need to iterate over
# every node every time the following visited node needed to be found. Instead could just pop off the top value in the MinHeap stack
# and result in a time and space complexity of.
# O((v + e) * log(v)) time | O(v) space
# The v + e comes from iterating through every node and every node's edges once, while the log(v) comes from finding the minimum not
# visited node at the end of every node. Ideally wouldn't need to contruct a MinHeap with proper functions and could just use built in 
# classes and functions though.