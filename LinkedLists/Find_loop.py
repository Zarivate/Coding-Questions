from tkinter import *
# Question:

# Given the head of a singly linked list that has a loop, a tail points to some node in the linked list
# instead of None/Null, write a function that returns the node (the actual node, not just the value itself)
# from which the loop originates in constant space.

# Example:

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

LL1 = LinkedList(0)
LL1.next = LinkedList(1)
LL1.next.next = LinkedList(2)
LL1.next.next.next = LinkedList(3)
LL1.next.next.next.next = LinkedList(4)
LL1.next.next.next.next.next = LinkedList(5)
# 5 points to 2
LL1.next.next.next.next.next.next = LL1.next.next

# LL1 = 0 --> 1 --> 2 --> 3 --> 4 --> 5 --
#                   ^                    |
#                   ---------------------|


# Answer:
# Node 2, which would return be 2 --> 3 --> 4 --> 5 --
#                               ^--------------------|


# Uncomment this code to show a print of the nodes, with 5 pointing back to 3
# print(LL1.value) # 0 -->
# print(LL1.next.value) # 1 -->
# print(LL1.next.next.value) # 2 -->
# print(LL1.next.next.next.value) # 3 -->
# print(LL1.next.next.next.next.value) # 4 -->
# print(LL1.next.next.next.next.next.value) # 5 -->
# print(LL1.next.next.next.next.next.next.value) # 2 -->

# For extra confirmation, here are the memory locations for node 2 and 5's pointer, they match up 
# meaning 5 is pointing to 2.
# print(LL1.next.next)
# print(LL1.next.next.next.next.next.next)


# Optimal Space & Time Complexity:
# O(n) time, because will need to iterate through the linked list at least 1 time to find the loop
# O(1) space, because the solution demands it, also because the solution is done in place


# Explanation:
# Through the power of pointers and big maths, this solution is done rather simply. Least in concept anyway...
# the main thing to realize is how, because we know for a fact there is a loop in the Linked list, we can
# use that to calculate the distance to the node where the loop originates. IE:

# Set 2 pointers, one will traverse at a regular rate while the second will traverse at twice the speed,
# keep traversing with both pointers until they're both at the same node. At that point, their paths can
# be broken down like so

# F = first pointer
# S = second pointer


# In the example created near the top, both nodes will converge at the 4 node, the paths both travel to get to the node
# differ but can be split up like so.
# D, The length from 0 to 2 (the looping node)
# P, The length from 2 to 4 (distance from the looping node to where the nodes met up)
# R, The remaining length of 4 to 2, distance between where the nodes met up to get back to the looping node

# Using the knowledge that, if F travels "x" nodes to get to 4, it will have traveled
# F = D + P

# Using the knowledge that S travels at twice the speed, "2x", it will have traveled
# S = 2D + 2P

# Because the goal is to get 1 full traversal since that way we'll be at the looping node, it will be called T
# and can be found by knowing how S took a loop and then some to get to the same position as the first pointer,
# by subtracting the distance from the looping node to where the pointers are, P, we can find where the looping
# node is as that would get us 1 full loop 
# T = S - P
# T = 2D + 2P - P
# T = 2D + P

# All that's left to find now is R, and since the total distance of 1 full loop can also be seen as 
# T = D + P + R (Because the remainder is what's left to traverse from where the pointers met to the looping node)
# R = T - D - P
# R = 2D + P - D - P
# R = D

# Meaning the remaining distance to get to the looping node, and thus the answer, is just D. Which can be traversed by 
# simply setting the first pointer to the start and then iterating both pointers, at the same rate now, until they
# match again. When that happens, either pointer can then be returned for an answer. IE:


# Both pointers meet up here at node 4
# LL1 = 0 --> 1 --> 2 --> 3 --> 4(S)(F) --> 5 --
#                   ^                    |
#                   ---------------------|

# Because the remainder, R, if traversed will get us to the looping node, and we know that R = D and that D can be 
# traversed by starting at the head and just iterating like normal, we just need to iterate from the start again till
# the nodes match again.


# Reset the first pointer, F, to the head of the linked list and iterate both pointers like normal till meet up again.
# IE:

# LL1 = 0(F) --> 1 --> 2 --> 3 --> 4(S) --> 5 --
#                      ^                       |
#                      ------------------------|

# LL1 = 0 --> 1(F) --> 2 --> 3 --> 4 --> 5(S) --
#                      ^                       |
#                      ------------------------|

# LL1 = 0 --> 1 --> 2(F)(S) --> 3 --> 4 --> 5 --
#                   ^                          |
#                   ---------------------------|


# Implementation:
def findLoop(head):

    # Set the two pointers
    first = head.next
    second = head.next.next

    # Keep iterating through the linked list with both pointers until they meet up
    while first != second:
        first = first.next
        second = second.next.next

    # Set the first pointer to be equal to the head again
    first = head

    # Keep iterating through both until they match up again
    while first != second:
        first = first.next
        second = second.next

    # Return the first pointer, should now be where the loop starts
    return first


print(findLoop(LL1).value)

# Visual example of problem alongside answer
window = Tk()
example_image = PhotoImage(file='LinkedLists/find_loop_visual.png')
example_label = Label(image=example_image)
example_label.pack()
window.mainloop()
