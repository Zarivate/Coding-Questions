# Question:

# Given the head of a Linked list with at least 1 node, write a function that returns its middle node.

# Note:
# For cases where the length of the Linked list is even, return the second of the middle nodes

# Example:
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


example = LinkedList(2)
example.next = LinkedList(7)
example.next.next = LinkedList(3)
example.next.next.next = LinkedList(1)

# Answer:
# LinkedList(3)
# (Because the length of the Linked list is even, meaning the middle node could be either 7 or 3 so 3 is returned)

example2 = LinkedList(1)
example2.next = LinkedList(4)
example2.next.next = LinkedList(7)
example2.next.next.next = LinkedList(5)
example2.next.next.next.next = LinkedList(9)


# Answer:
# LinkedList(7)
# (Because the length of the Linked list is odd, 5, 5/2 = 2.5, but floored would be 2, meaning the middle node
# must be 7.)

# Optimal Space & Time Complexity:
# O(n) time (Because will only iterate through Linked list once)
# O(1) space (No extra space needed to get solution)
# n = number of nodes in Linked list


# Explanation:
# The main thing to realize is how, no matter what, in order to find the middle node you'll need to know the length
# of the Linked list. Because the LinkedList class doesn't have a len property however, you'll have to iterate through
# it at least one time to get the length. Once you have that, you can just divide the length by 2, floor it, and iterate
# through the Linked list again up until that number and return that node. Important to note that flooring even in the
# case of even numbers gets the correct answer still. Can be seen in the example problems, where length = 4 and
# length = 5 for examples 1 and 2. 4/2 floored = 2, which would point to node 3 in the first example. 5/2 = 2.5 floored,
# which would be 2 that points to node 7 in the second example.

# While this approach does work and would still use the optimal amount of space and time, there is another slightly
# cleaner way. It involves 2 pointers and works by moving one of them at double the rate of the other. That way, by the
# time the pointer that's twice as fast reaches either the end of the Linked list (.next = null) or a null node in
# general (node = null), the slower pointer will be in the middle. IE:

# Example1: 2 --> 7 --> 3 --> 1
# pointer_slow = 2
# pointer_fast = 2
# Move the slower pointer by 1 while the faster by 2
# pointer_slow = 7
# pointer_fast = 3
# Move the slower pointer by 1 while the faster by 2
# pointer_slow = 3
# pointer_fast = null
# Return LinkedList(3)

# Example2: 1 --> 4 --> 7 --> 5 --> 9
# pointer_slow = 1
# pointer_fast = 1
# Move the slower pointer by 1 while the faster by 2
# pointer_slow = 4
# pointer_fast = 7
# Move the slower pointer by 1 while the faster by 2
# pointer_slow = 7
# pointer_fast = 9 (9.next = null so finished)
# Return LinkedList(7)

# Will just need to keep in mind that the faster pointer is either at None or it's .next value will be None.


# Implementation:
def middle_node_clean(linked_List):
    # Initialize two pointers, each starting at the head of the Linked list
    pointer_slow = linked_List
    pointer_fast = linked_List
    # Iterate through the Linked list until the faster pointer is either None or it's .next value is None
    while pointer_fast and pointer_fast.next:
        # Iterate the slow pointer by 1
        pointer_slow = pointer_slow.next
        # Iterate the faster pointer by 2
        pointer_fast = pointer_fast.next.next

    return pointer_slow.value


print(middle_node_clean(example))
print(middle_node_clean(example2))


# Bonus not as clean answer:
def middle_node_bonus(linked_list):
    length = 0
    current_node = linked_list
    while current_node is not None:
        length += 1
        current_node = current_node.next

    middle_node = linked_list
    for _ in range(length // 2):
        middle_node = middle_node.next

    return middle_node.value


print(middle_node_bonus(example))
print(middle_node_bonus(example2))
