# Question:

# Given 2 linked lists of possible unequal length, where each represent a non-negative integer where
# each node is a digit of that entire integer. Write a function that returns the head of a new linked
# list that represents the sum of the 2 linked lists. 


# Notes:
# Not allowed to modify either of already existing Linked Lists
# The value of each node is between 0 and 9
# Because of the way that the numbers are structured, in least to most significant order, the head that'll be returned will be
# the start of the number, IE: 512, 2 would be the head because it would go like so.
# Singles (2), Tens (1), Hundreds (5), 2 --> 1 --> 5 which would be 512

# Example:
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# This linked list represents the number 4973
link_1 = LinkedList(3)
link_1.next = LinkedList(7)
link_1.next.next = LinkedList(9)
link_1.next.next.next = LinkedList(4)


# This linked list represents the number 512
link_2 = LinkedList(2)
link_2.next = LinkedList(1)
link_2.next.next = LinkedList(5)


# Answer: (5485) (4973 + 512 = 5485)
link_3 = LinkedList(5) # This head node would be what is returned
link_3.next = LinkedList(4)
link_3.next.next = LinkedList(8)
link_3.next.next.next = LinkedList(5)



# Explanation:
# For this one, conceptually it can be solved quite simply, that being to add the numbers simultaneously while also
# creating the nodes for them, but a few things need to be kept in mind when doing so.

# Have to account for any carries/leftovers when adding (IE: Nodes can only be value 0-9, so something like 10 and up won't work)
# Need to create something like a dummy node so can return the head of newly created Linked List
# Account for any out of bound errors when iterating through both Linked lists, as they may not be the same length.


# Breakdown:

# LL1 = 3 -> 7 -> 9 -> 4
# LL2 = 2 -> 1 -> 5

# Create the needed variables
# carry = 0
# dummyNode = LinkedList(0), 0 -->
# currentNode = dummyNode, 0

# Iterate through both LLs simultaneously and add their values together alongside the carry and also modulate it by 10 in case it's over 10
# LL1 = 3(here) -> 7 -> 9 -> 4
# LL2 = 2(here) -> 1 -> 5
# sum = 3 + 2 + carry = 3 + 2 + 0 = 5 % 10 = 5
# sum = 5

# Create a new node from the calculated sum
# newNode = LinkedList(sum) = LinkedList(5)

# Set the currentNode to point to the newly created node. 
# currentNode.next = newNode, 0 --> 5

# Set the current node to be equal to the newly made one
# currentNode = 5, 0 --> 5(here)

# To get the carry of any number it would just be the sum divided by 10 and then floored, so do that on the sum to get the new carry
# carry = sum // 10 = 5 // 10 = 0
# carry = 0


# Repeat process till finished
# LL1 = 3 -> 7(here) -> 9 -> 4
# LL2 = 2 -> 1(here) -> 5
# sum = 8 (7 + 1 + 0 % 10 = 8)
# newNode = LinkedList(8)
# currentNode.next = newNode, 0 --> 5 --> 8
# currentNode = 8, 0 --> 5 --> 8(here)
# carry = 0 (7 + 1 + 0 // 10 = 0)


# LL1 = 3 -> 7 -> 9(here) -> 4
# LL2 = 2 -> 1 -> 5(here)
# sum = 4 (9 + 5 + 0 % 10 = 14 % 10 = 4)
# newNode = LinkedList(4)
# currentNode.next = newNode, 0 --> 5 --> 8 --> 4
# currentNode = 8, 0 --> 5 --> 8 --> 4(here)
# carry = 1 (9 + 5 + 0 = 14 // 10 = 1)


# ***************************************************************************
# Very important, now when trying to iterate to following node in LLs will see that are at the end of the 2nd LL.
# To avoid any out of bound errors when iterating through, will have to check to see if following node exists or not,
# if not then just set it to be None/0.
# ***************************************************************************
# LL1 = 3 -> 7 -> 9 -> 4(here)
# LL2 = 2 -> 1 -> 5 --> 0(here)
# sum = 5 (4 + 0 + 1 % 10 = 5 % 10 = 5)
# newNode = LinkedList(5)
# currentNode.next = newNode, 0 --> 5 --> 8 --> 4 --> 5
# currentNode = 5, 0 --> 5 --> 8 --> 4 --> 5(here)
# carry = 0 (4 + 0 + 1 = 5 // 10 = 0)


# By now will have reached end of both LLs and can just return the pointer of the dummyNode for the head of the new LL



# Optimal Space & Time Complexity:
# O(max(n,m)) time | O(max(n,m)) space
# n = length of 1st Linked List
# m = length of 2nd Linked List



# Optimal Solution:
def sumLinkedLists(LL1, LL2):
    # Create the necessary variables
    dummyNode = LinkedList(0)
    currentNode = dummyNode
    carry = 0

    # Set the nodes to be the heads of the input LLs, will be used to traverse through each
    nodeOne = LL1
    nodeTwo = LL2
    # So long as any nodes still need to be traversed in either LL or the carry isn't 0 yet, loop will continue
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        # In the event that either nodeOne or nodeTwo are None and thus don't have values, set the values to be 0,
        # else let them be whatever value they'd normally be.
        valOne = nodeOne.value if nodeOne is not None else 0
        valTwo = nodeTwo.value if nodeTwo is not None else 0

        # Add the two values together
        sum = valOne + valTwo

        # Modulate the sum to get the remainder in case any value is above 10
        newSum = sum % 10
        # Create a new node from the newly calculated sum
        newNode = LinkedList(newSum)
        # Set the currentNode to point to the newly created node
        currentNode.next = newNode
        # Set the currentNode to be the newly created node
        currentNode = newNode

        # Get the floor of whatever is left after dividing the sum by 10, IE: The carry
        carry = sum // 10
        
        # In the event that the end of either LL has been reached, to avoid any out of bouns errors, 
        # check to see if the following node in the LL exists, if so just set it equal to that, else
        # set it equal to None.
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return dummyNode.next.value




print(sumLinkedLists(link_1, link_2))