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

