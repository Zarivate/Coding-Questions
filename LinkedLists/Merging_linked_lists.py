# Merging linked lists

# Question:
#   Given 2 Linked Lists of possible different length, they possibly merge at some point.
#   Every Linked Lists node has an integer with a "value" alongside a "next" node pointing
#   to the next node if there is one, if not then it points to "null/none". Write a function
#   that returns the point at which the Linked Lists meet, if at all, else return None/null.

# Requirements
#   Should return an existing node, if one exists
#   Shouldn't modify any Linked Lists
#   Shouldn't create any new Linked Lists either

# Example
# LL1 = 2 -> 3 -> 7 -> 5
# LL2 = 4 -> 7 -> 5

# Example answer:
# 7 -> 5 because they intersect at the third node that has a value of 7

# Things to make note of:
#   Any nodes before intersection node are not shared, while any after are
#   The first matching node is also the intersection node/the answer

# Ways to solve:
# 1. Could just iterate through each linked lists until find first node that matches. Could take a pointer and start at
# any linked list while keeping track of nodes as you go by using a Set. Since any values held within the set would be
# a node that, not only holds the current value, but also holds the next value it's pointing at.

# IE: LinkListOneNodes = {2} -> LinkListOneNodes = {2, 3} -> LinkListOneNodes = {2, 3, 7} ->
# LinkListOneNodes = {2, 3, 7, 5} -> Node of value 5 points to Null/none so no longer add values to Set.
# Iterate through second Linked List, see that 4 doesn't exist in Set so move on to 7 and see that it does exist
# within the Set already so return that node. Else if you couldn't find a matching node then return Null/none.

# Space Time Complexity:
#   O(n+m) time (because iterating through lengths of both lists)
#   O(n) space (because creating a data structure to hold "n" variables of a linked list)


# 2. Similar idea but now without the use of an extra data structure. Instead, answer can be found by using
# the knowledge that from the intersection point onwards, the length of the two linked lists is the same. Meaning
# that by calculating the difference in their lengths, the intersection can be found. Would still have to iterate
# through both linked lists to get the lengths, however from that point on can use the discovered difference in
# their lengths to arrive to the intersection node in 1 shot.

# IE: The length of the first linked list in the example is 4, while the length of the second is 3. The difference
# between these two would be 1. Meaning the first Linked List has 1 more node than the second. After finding this by
# iterating through both lists one time. Start at the longer linked list and move up however many nodes the difference
# is. Would go like so
# LL1: 2 -> would move 1 up to now point at 3,
# LL1: 3 ->
# Can now start iterating through the second linked list, would start at
# LL2: 4 ->
# Can now iterate through both at the same time and automatically reach the intersection point
# LL1: 3 -> 7, LL1: 7
# LL2: 4 -> 7, LL2: 7
# Can now return the 7 node to get an answer of 7 -> 5

# Space Time Complexity:
# O(n+m) time (since still iterating through both linked lists
# O(1) space (since no longer using any extra space that scales depending on the size of the input/linked list size


# 3. Big brain way to solve
# Same idea as previous way, only now you ignore having to calculate any lengths of the sort by having the pointers
# that iterate through the two linked lists wrap around each other once they reach the end of their respective lists.
# Effectively making them go through the same amount of nodes to reach the intersection node at the same time.

# IE: Imagine there are pointers for each linked list iterating through their respective LL at the same time. Since the
# second LL is shorter than the first, it'll reach its end before the first one like so
# LL1: 2 -> 3 -> 7 (pointer is here) -> 5
# LL2: 4 -> 7 -> 5 (pointer is here)
# Instead of making the pointer for LL2 stop, have it point to the start of the start of LL1 to get
# LL1: 2 (Pointer 2 here) -> 3 -> 7 -> 5 (Pointer 1 here)
# LL2: 4 -> 7 -> 5
# Do the same for the first pointer once it reaches the end of its own linked list to get
# LL1: 2 -> 3 (Pointer 2 here) -> 7 -> 5
# LL2: 4 (Pointer 1 here) -> 7 -> 5
# Iterate both pointers to get them to point to the same node, 7
# LL1: 2 -> 3  -> 7 (Pointer 2 here) -> 5
# LL2: 4  -> 7 (Pointer 1 here) -> 5

# Space Time Complexity:
# O(n+m) time (since still iterating through both linked lists)
# O(1) space (same reason as before, no scaling extra space)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


LL1 = LinkedList(1)
LL1.next = LinkedList(2)
LL1.next.next = LinkedList(3)
LL1.next.next.next = LinkedList(4)
LL1.next.next.next.next = LinkedList(5)
LL1.next.next.next.next.next = LinkedList(6)
print()
LL2 = LinkedList(0)
LL2.next = LinkedList(9)
LL2.next.next = LinkedList(3)
LL2.next.next.next = LinkedList(4)
LL2.next.next.next.next = LinkedList(5)
LL2.next.next.next.next.next = LinkedList(6)

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
print_linked_list(LL2)
print()


# Array to be made into Linked Lists in combination with function the values here to do more testing
# arr = [1, 2, 3, 4, 5, 6]
# arr2 = [0, 7, 9, 3, 4, 5, 6]


# Dummy function to automatically make linked lists from an array
# def make_linked_list(sample_array=None, sample_node=LinkedList(0)):
#     while sample_array and sample_array[0] is not None:
#         print("The passed in array is " + str(sample_array))
#         sample_array.pop(0)
#         print("The passed in array is now " + str(sample_array))
#         print("The node value passed in is " + str(sample_node.value))
#         print(sample_node.next)
#         sample_node.next = LinkedList(sample_array[0])
#         print(sample_node.next.value)
#         print()
#         make_linked_list(sample_array, sample_node.next)
#     return sample_node.next
#
#
# make_linked_list(arr, LL1)


def merging_linked_lists(linkedListOne, linkedListTwo):
    pointerOne = linkedListOne

    pointerTwo = linkedListTwo

    while pointerOne.value is not pointerTwo.value:
        # Show the values as they iterate through the linked lists
        print("Pointer one is currently at node " + str(pointerOne.value))
        print("Pointer two is currently at node " + str(pointerTwo.value))

        # If pointerOne has reached the end of the first linked list, will have a value of none/null
        if not pointerOne:
            pointerOne = linkedListTwo
        else:
            pointerOne = pointerOne.next

        if not pointerTwo:
            pointerTwo = linkedListOne
        else:
            pointerTwo = pointerTwo.next

    if pointerOne is not None:
        print()
        print("Pointer one is now at node " + str(pointerOne.value))
        print("Pointer two is now at node " + str(pointerTwo.value))
        print("They're now at the same node, thus we can end.")
    else:
        print("Null value")
    return pointerOne


merging_linked_lists(LL1, LL2)
