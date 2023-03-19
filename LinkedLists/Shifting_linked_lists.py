# Question:
# Write a function that takes in the head of a singly linked list and an integer "k", that caa be either positive or
# negative, and shifts the list in place by "k" positions, and returns it's new head

# Note(s):
# "k" can be positive or negative
# Can assume input LL will have at least 1 node, in other words the head will never be None/null

# Example:
# head = 0 --> 1 --> 2 --> 3 --> 4 --> 5
# k = 2

# Answer:
# head = 4 --> 5 --> 0 --> 1 --> 2 --> 3 (Have a new head of value 4)

# Optimal Space Time Complexity:
# O(n) time (n = number of nodes in the input LL)
# Can also tell this will be an O(n) time question because of how, the tail is needed for the answer, but because it's
# not given, we have to traverse the LL to get it.
# O(1) space (because can solve without using any extra scaling memory)

# Explanation:
# Important thing to take away first off is how only 4 nodes are really needed from the example in order to get to the
# solution. Nodes 0, 3, 4, and 5.
# Need 0 because 5 needs to point to it
# Need 4 because it's the new head
# Need 3 because it'll be the new tail, and has direct access/points to 4
# Tricky thing is how to get these nodes, keep track of them, and what to do about edge cases




