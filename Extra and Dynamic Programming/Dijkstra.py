import sys
import os
from dotenv import load_dotenv

load_dotenv()
resizePath = os.getenv("RESIZEPATH")

sys.path.insert(1, resizePath)
from resizeImg import *
# Question

# Given an adjacency list representing a graph and an integer "start" value. Utilize Djikstra's algorithm to find the 
# shortest paths to each vertice in the graph and returns them in an array. Where the index of the array represents the
# shortest path to that designated index. If there is no path to the vertice/index, -1 should be placed in it's position 
# in the answer array.

# Notes:

# No self loops
# No negative weights/edges
# All edges are directed in 1 direction only
# Length of adjacency list=number of vertices in graph, IE: In example length of list is 6 with vertices 0-5

# Example:
start = 0

edges = [
    [[1, 7]], # This represents vertex 0, that has one outgoing edge to 1 with a weight of 7
    [[2, 6], [3, 20], [4, 3]], # This represents vertex 1 with 3 outgoing edges, an edge to 2 with a weight of 6, edge to 3 with weight of 20, and edge to 4 with weight of 3
    [[3, 14]], # This represents vertex 2, that has one outgoing edge to 3 with a weight of 14
    [[4, 2]], # This represents vertex 3, that has one outgoing edge to 4 with a weight of 2
    [],
    [],
]

# Visual example of problem
img_path = "Extra and Dynamic Programming\dijkstrasalgorithmexample.png"
imgResizeHalf(img_path, "Dijikstra's Algorithm Example")

# Answer
# [0, 7, 13, 27, 10, -1]


# Optimal Space & Time Complexity:
# O((v + e) * log(v)) time | O(v) space
# v = Number of vertices
# e = Number of edges

