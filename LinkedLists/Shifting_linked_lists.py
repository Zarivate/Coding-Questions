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

# Case when "k" is a positive integer
# The Pointer to The New Tail (PNT) can be found by traversing the list once to get the length,
# which can be used to find the original tail at the same time, using the formula
# PNT = length - k, for example in the sample question

# PNT = 6 - 2 = 4 --> 3 (The 4th position in the original un shifted linked list is at value 3)
# Head (given to us) = 0
# Tail (found after 1 traversal of list) = 5
# New Tail (PNT) = 3
# New Head = 4 (3 has access to 4 via ".next")

# Now just need to do a few operations to get the new linked list
# *****************************
# New Head = new tail.next              3 --> 4 (new Head)
# new tail.next = null                  3 --> null (new tail)
# (old) tail.next = head                5 --> 0 (because 3 now points to null and not 4, we'll have 4 --> 5 --> 0)
# return new head                       4 --> 5 --> 0 --> 1 --> 2 --> 3
# *****************************

# Special cases
# *****************************
# If k = 0 or a multiple of the length
# Nothing needs to be done, as everything would be shifted and end up exactly where it already was

# *****************************
# If k = Number larger than length
# use modulo operator to get smaller k, IE:
# k = 30
# length = 6
# 15 % 6 = 3 (6 goes into 15 2 times for 12, 15 - 12 = 3)
# new k = 3

# *****************************
# If k = -Number
# Formula changes, goes from new k = k % length to
# new k/new tail position = k, (just make it positive) IE:
# k = -2 would become k = 2
# 0 --> 1 --> 2 --> 3 --> 4 --> 5
# 2 % 6 = 2, value at 2nd position is 1 which would be the new tail
# would become
# 2 --> 3 --> 4 --> 5 --> 0 --> 1

# Optimal Solution:
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Using the input example for some comment notes
def shiftLinkedList(head, k):
    # Variable to store input string's length for later
    length = 1
    # Value to hold the original tail, starts at head but will be updated to the last value in the linked list later
    original_tail = head

    # While loop that goes until end of linked list
    while original_tail.next is not None:
        # Update variable until at last value in linked list
        original_tail = original_tail.next
        # Update length till have full length of linked list
        length += 1

    # Now that have linked list length, use formula to discover what the offset/shift value should be
    new_k = abs(k) % length
    # If you get 0 then just return what was already sent in as there is no need to shift anything
    if new_k == 0:
        return head

    # Calculate the position of the new tail while accounting for any special cases, such as negative k values
    # IE: If k is positive, do length -k, else just use the new_k value as the position
    new_tail_position = length - new_k if k > 0 else new_k
    # Variable to store the future tail, will start at the head/first node as usual
    new_tail = head

    # For loop that goes until the new tail position is reached
    for i in range(1, new_tail_position):
        # Update new_tail variable until the new tail is reached
        new_tail = new_tail.next    #

    # Now just have to make sure the nodes and their pointers are swapped correctly

    # The new head becomes equal to the pointer of the new tail
    new_head = new_tail.next    # 3 --> 4 (new_head)
    new_tail.next = None        # 3 --> None
    original_tail.next = head   # 5 --> 0
    print_linked_list(new_head)
    return new_head             # 4 --> 5 --> 0 --> 1 --> 2 --> 3


LL1 = LinkedList(0)
LL1.next = LinkedList(1)
LL1.next.next = LinkedList(2)
LL1.next.next.next = LinkedList(3)
LL1.next.next.next.next = LinkedList(4)
LL1.next.next.next.next.next = LinkedList(5)

# Function to print out the values
def print_linked_list(item):
    # base case
    if item is None:
        return
    # Print current node
    print(item.value)
    # Print following node
    print_linked_list(item.next)


print_linked_list(LL1)
print()

shiftLinkedList(LL1, 2)




