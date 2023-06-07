# Question:

# Given a node class that has a name and an array of optional children nodes, implement a Breadth First Search (BFS)
# method that takes in an empty array, traverses it going from left to right, stores all the node names within the
# input array and returns it.


# Example:

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
# The code below should create a graph that looks like so    
# TODO: Implement visual example here    
example_graph = Node("A")
example_graph.addChild("B").addChild("C").addChild("D")
example_graph.children[0].addChild("E").addChild("F")
example_graph.children[2].addChild("G").addChild("H")
example_graph.children[0].children[1].addChild("I").addChild("J")
example_graph.children[2].children[0].addChild("K")


# Answer:

# ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]


# Explanation:
# Main idea to realize for this problem is how valuable a queue would be due to it's First In First Out (FIFO)
# property. In other words, if you were to append to the queue in order of a parent node first, then pop it off,
# and append to the stack it's children nodes, and continue like so, the queue would be traversed in a BFS way. 
# To fill the input array all you would need to do is append to the array the name of every node as they're being
# popped off the queue. IE:

# TODO: Implement visual showing popping off a node, adding it to a queue, then popping it off the queue, appending
# it's name to the input array, then appending it's children node's to the queue. Essentially make visual of first
# example in notebook


# Queue = [A], set Queue to be equal to the head of the graph at the start
# input_array = []

# Queue = [], pop node A off stack using FIFO property
# input_array = [A], append name to input array
# Queue = [B, C, D], append A's children nodes to stack and continue

# Queue = [C, D], pop node B off stack using FIFO property
# input_array = [A, B], append name to input array
# Queue = [C, D, E, F], append B's children nodes to stack and continue

# Queue = [D, E, F], pop node C off stack using FIFO property
# input_array = [A, B, C], append name to input array
# Queue = [D, E, F], append C's children nodes to stack and continue (C has no children node in example)

# Queue = [E, F], pop node D off stack using FIFO property
# input_array = [A, B, C, D], append name to input array
# Queue = [E, F, G, H], append D's children nodes to stack and continue

# Queue = [F, G, H], pop node E off stack using FIFO property
# input_array = [A, B, C, D, E], append name to input array
# Queue = [F, G, H], append E's children nodes to stack and continue (E is leaf node so no nodes to add)

# Queue = [G, H, I, J], pop node F off stack using FIFO property
# input_array = [A, B, C, D, E, F], append name to input array
# Queue = [G, H, I, J], append F's children nodes to stack and continue

# Queue = [H, I, J], pop node G off stack using FIFO property
# input_array = [A, B, C, D, E, F, G], append name to input array
# Queue = [H, I, J, K], append G's children nodes to stack and continue (G has only 1 node so only append K)

# Queue = [I, J, K], pop node H off stack using FIFO property
# input_array = [A, B, C, D, E, F, G, H], append name to input array
# Queue = [I, J, K], append H's children nodes to stack and continue (H has 0 children nodes so append nothing)

# Queue = [J, K], pop node I off stack using FIFO property
# input_array = [A, B, C, D, E, F, G, H, I], append name to input array
# Queue = [J, K], append I's children nodes to stack and continue (I has 0 children nodes so append nothing)

# Queue = [K], pop node J off stack using FIFO property
# input_array = [A, B, C, D, E, F, G, H, I, J], append name to input array
# Queue = [K], append J's children nodes to stack and continue (J has 0 children nodes so append nothing)

# Queue = [], pop node K off stack using FIFO property
# input_array = [A, B, C, D, E, F, G, H, I, J, K], append name to input array
# Queue = [], append K's children nodes to stack and continue (K has 0 children nodes so append nothing)

# Queue is now empty meaning have travered all the nodes so can return input array as answer



# Optimal Space & Time Complexity:
# O(v + e) time | O(v) space
# v = # of vertices/nodes of input graph
# e = # of edges of input graph


# Breakdown:
# O(v + e) time
# O(v) from eventually having to traverse every node
# O(e) from having to loop through every child node, where the number of children nodes is dependent on the # of edges a node has

# O(v) space
# O(v) from the worst case being where graph is just 1 level below head node. Meaning the queue will be of size v-1, which rounds
# down to just v. IE:
# TODO: Add visual example of worst case scenario graph


# Implementation:
def breadth_first_search(self, array):

    # Set the queue to be equal to the head of the passed in graph
    queue = [self]

    # While loop to continue until queue is empty
    while len(queue) > 0:
        # Set the current node to be equal to the node at the head of the queue, IE: First one in
        current_node = queue.pop(0)
        # Append the current node's name to the array
        array.append(current_node.name)
        # Loop through the current node's children nodes and append them to queue
        for child in current_node.children:
            # Append the child to the queue
            queue.append(child)

    return array


print(breadth_first_search(example_graph, array=[]))
