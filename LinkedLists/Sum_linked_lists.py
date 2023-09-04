# Question:

# Given 2 linked lists of possible unequal length, where each represent a non-negative integer where
# each node is a digit of that entire integer. Write a function that returns the head of a new linked
# list that represents the sum of the 2 linked lists. 


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

# Answer: (5485)
link_3 = LinkedList(5) # This head node would be what is returned
link_3.next = LinkedList(4)
link_3.next.next = LinkedList(8)
link_3.next.next.next = LinkedList(5)


# Explanation:



# Optimal Space & Time Complexity:
# O 