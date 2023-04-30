# Question:

# Given the head of a singly linked list, and without using any auxiliary data structure, write a function that returns
# a boolean representing whether the Linked list is a palindrome or not.

# Notes:
# For linked lists, they're palindromes when their node values are the same when read from left to right and right to
# left.
# Single node linked lists are palindromes.
# Given linked lists will always have at least 1 node/will never be empty
# Allowed to modify linked list

# Example:
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


example1 = LinkedList(1)
example1.next = LinkedList(2)
example1.next.next = LinkedList(3)
example1.next.next.next = LinkedList(3)
example1.next.next.next.next = LinkedList(2)
example1.next.next.next.next.next = LinkedList(1)


# Answer:
# True
# (Looks like this 1 --> 2 --> 3 --> 3 --> 2 --> 1)
# Numbers read from left to right are 1, 2, 3, 3, 2, 1
# Numbers read from right to left are 1, 2, 3, 3, 2, 1


# Optimal Space & Time Complexity:
# O(n) time
# O(1) space
# n = number of nodes in linked list


# Explanation:
# To begin, should first see what would be done if the question was slightly different.
# If it was a string palindrome, IE:
# "123321"
# We could just use 2 pointers, one at the start and another at the end and compare each value while slowly
# incrementing and decrementing the pointers respectively until they either don't match or cross each other. Like so,
# pointer_one = 1 (1(here) --> 2 --> 3 --> 3 --> 2 --> 1)
# pointer_two = 1 (1 --> 2 --> 3 --> 3 --> 2 --> 1(here))
# Increment and decrement the respective pointers until they eventually cross each other due to being the same, would
# prove that is a palindrome.

# If we could use some sort of auxiliary data structure like a stack, then could iterate through the linked list one
# time to populate the stack with the nodes, where, because a stack is a LIFO data structure, the end of the linked
# list will be at the top. Meaning we can iterate through the linked list one more time and check to see if the nodes
# match up, if so then will know it's a palindrome. IE:
# 1 --> 2 --> 3 --> 3 --> 2 --> 1
# stack = [1, 2, 3, 3, 2, 1]
# Now iterate through linked list while comparing the values in the stack to see if they match up
# 2 --> 3 --> 3 --> 2 --> 1
# stack = [1, 2, 3, 3, 2]
# 3 --> 3 --> 2 --> 1
# stack = [1, 2, 3, 3]
# 3 --> 2 --> 1
# stack = [1, 2, 3]
# 2 --> 1
# stack = [1, 2]
# 1
# stack = [1]
# All match up so can return True

# While we can't use any auxiliary data structure, we can replicate it through recursion and a call stack to get the
# answer the same way. IE: A recursive call stack could mimic the same function

# It would work similarly but with the recursive call being done on the node that is being compared, since we start at
# the beginning of the linked list and would need to compare it to the nodes at the end, the calls would look something
# like this.

# recursive_call(left_node, right_node)
# recursive_call(head, head)
# recursive_call(head, head.next), up until the base case is reached where head.next is Null/end of linked list
# recursive_call(1, 1) 1(both are here) --> 2 --> 3 --> 3 --> 2 --> 1
# recursive_call(1, 2) 1 --> 2(this one) --> 3 --> 3 --> 2 --> 1
# recursive_call(1, 3) 1 --> 2 --> 3(this one) --> 3 --> 2 --> 1
# recursive_call(1, 3) 1 --> 2 --> 3 --> 3(this one) --> 2 --> 1
# recursive_call(1, 2) 1 --> 2 --> 3 --> 3 --> 2(this one) --> 1
# recursive_call(1, 1) 1 --> 2 --> 3 --> 3 --> 2 --> 1(this one)
# recursive_call(1, null) 1 --> 2 --> 3 --> 3 --> 2 --> 1 --> null(this one)


# By now, call stack will begin to unwind and return. Each call will return 2 things, either True or False and the
# node that is being compared to, IE:
# recursive_call(1, null) --> True, 1, gets returned to recursive_call(1,1).
# 1 --> 2 --> 3 --> 3 --> 2 --> 1 (this one is returned because is left node of null) --> null
# What will happen now is that the following recursive call will compare whatever left node was returned to whatever
# is the right node of the following call. IE: '
# Will compare 1 --> 2 --> 3 --> 3 --> 2 --> 1 (this one) to recursive_call(1,1(this one)) to get

# recursive_call(1,1) --> True, 2,
# 1 --> 2 --> 3 --> 3 --> 2 (now returns this to subsequent recursive call) --> 1

# Can also be seen as returning 2 because the following left node would be 2. In other words, for the call of
# recursive_call(1,1) are comparing 1(this one) --> 2 --> 3 --> 3 --> 2 --> 1(this one) for
# recursive_call(1, 2) are comparing 1 --> 2(this one) --> 3 --> 3 --> 2(this one) --> 1
# Because of how the right of this call is 2, while the left node returned from the last call
# (recursive_call(1,1)) was T,2

# recursive_call(1, 2) --> T, 3     1 --> 2(left) --> 3 --> 3 --> 2(right) --> 1
# recursive_call(1, 3) --> T, 3     1 --> 2 --> 3(left) --> 3(right) --> 2 --> 1
# recursive_call(1, 3) --> T, 2     1 --> 2 --> 3(right) --> 3(left) --> 2 --> 1
# recursive_call(1, 2) --> T, 1     1 --> 2(right) --> 3 --> 3 --> 2(left)--> 1
# recursive_call(1, 1) --> T, 1     1(right) --> 2 --> 3 --> 3 --> 2 --> 1(left)
# By now back at head of Linked list and will have either bubbled up True or False through the call stack,
# just have to return it now

# Time & Space Complexity:
# O(n) space (Because size of call stack will at most be the size of the number of nodes in the linked list)
# O(n) time (Have to iterate through linked list at least once)


# Implementation:
def linked_list_palindrome_recursive(head):
    # Store the call answer in a variable
    answer = is_palindrome_recursive(head, head)
    # Return whether all the nodes matched up or not
    return answer.outer_nodes


def is_palindrome_recursive(left_node, right_node):
    # Base case where right node is empty/null
    if right_node is None:
        # If so return True alongside the passed in left node
        return LinkedListInfo(True, left_node)

    # Recursive call until the end of the linked list is reached in right_node.next
    recursive_result = is_palindrome_recursive(left_node, right_node.next)
    # Variable to hold whether the current left and right nodes were equal to each other
    left_comparison = recursive_result.left_compare
    # Separate variable to hold whether the nodes outside the current compared ones were equal or not
    outer_nodes_are_equal = recursive_result.outer_nodes

    # Variable to hold whether both the outer nodes were equal and the current left node and right node. This is to
    # bubble up any possible Falses found during calls.
    recursive_is_equal = outer_nodes_are_equal and left_comparison.value == right_node.value
    # Increment the left pointer to the following node
    next_left_comparison = left_comparison.next

    #
    return LinkedListInfo(recursive_is_equal, next_left_comparison)


# Class to hold whether the left node to be compared to and whether the other compared nodes were equal or not.
class LinkedListInfo:
    def __init__(self, outer_nodes, left_node_to_compare):
        self.outer_nodes = outer_nodes
        self.left_compare = left_node_to_compare


print(linked_list_palindrome_recursive(example1))


# Optimal Approach: Iterative.

# The idea for this solution is the same as the recursive one, where the goal is to loop backwards through the linked
# list. The main idea is to reverse half of the linked list, and then iterate through both halves at the same time
# and see if the values are the same, if so then is a palindrome, else is not. IE:

# Would turn
# 1 --> 2 --> 3 --> 3 --> 2 --> 1
# into
# 1 --> 2 --> 3 --> 1 --> 2 --> 3
# Then could just take two pointers
# 1(one here) --> 2 --> 3 --> 1(another here) --> 2 --> 3
# And iterate through like normal and see if values match up

# How would this be done? Well would first need to know where the middle/head of the linked list to be reversed
# is at. To find this, can call back to the Middle_node problem by using 2 pointers, one slow and another that iterates
# through twice as fast. IE:

# 1(slow pointer) (fast pointer) --> 2 --> 3 --> 3 --> 2 --> 1
# 1 --> 2(slow) --> 3(fast) --> 3 --> 2 --> 1
# 1 --> 2 --> 3(slow) --> 3 --> 2(fast) --> 1
# 1 --> 2 --> 3 --> 3(slow) --> 2 --> 1 --> null (fast)

# Now that have the head of the linked list half to reverse, can pass it to a function that could reverse it. To reverse
# a linked list, 3 pointers are needed.

# One to the previous node, prev = null
# One to the current, current = 3
# One to the following, next = 2

# Would then need to follow a few simple steps
# Make the current.next = prev,                                 current.next = null
# Make the previous node the current, prev = current            prev = 3
# Make the current become the next, current = next              current = 2
#                                                               next = 2 (still, will be changed in next iteration)
#                           1 --> 2 --> 3 --> 3 --> null  2 --> 1


# Repeat, this time alter next now though
# Make the next value equal to the current.next,                next = 1
# Make the current.next = prev,                                 current.next = 3
# Make the previous node the current, prev = current            prev = 2
# Make the current become the next, current = next              current = 1

#                           1 --> 2 --> 3 --> 3 --> null  --- 2     1
#                                              <----------

# Repeat
# Make the next value equal to the current.next,                next = null
# Make the current.next = prev,                                 current.next = 2
# Make the previous node the current, prev = current            prev = 1
# Make the current become the next, current = next              current = null
#                           1 --> 2 --> 3 --> 3 --> null  --- 2 <-- 1 (returned head)
#                                              <----------

# Can now return prev, as head of newly reversed linked list

# Now that have references to both heads of these linked lists, can iterate through both until either find a mismatch
# or reach end of one of them.


# Implementation:
def linked_list_palindrome_iterative(head):
    # Create two pointers, one to iterate through the linked list normally and another to do so twice as fast
    slow_pointer = head
    fast_pointer = head
    # While loop to iterate through linked list until faster pointer is either null or is about to be null
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # Reverse the second half of the linked list
    reversed_head = reverse(slow_pointer)
    # Create a new variable to hold the original first half of the linked list
    original_half = head

    # Iterate until at the end of the reversed half
    while reversed_head is not None:
        # If at any points the values from either sides don't match up, return False
        if reversed_head.value != original_half.value:
            return False
        # Else iterate through both halves
        reversed_head = reversed_head.next
        original_half = original_half.next

    return True


# Function to reverse the second half of the linked list
def reverse(head):
    # Variable to hold an empty node
    prev = None
    # Variable to hold the current node
    current = head
    # Continue until the current node had gone through all the other nodes/is empty
    while current is not None:
        # Set the next node to be the current's.next
        next_node = current.next
        # Set the following node to be the previous one
        current.next = prev
        # Set the previous node to be the current node
        prev = current
        # Set the current node to be equal to the now changed next_node
        current = next_node
    # Return the new head of the reversed linked list
    return prev


print(linked_list_palindrome_iterative(example1))
