# Question:
# Write a function that accepts an array of integers representing a stack, recursively sorts the stack in place,
# and returns it.

# Note:
# Array must be treated as a stack, with the end of the array representing the top of the stack
# Only allowed to do 3 certain operations to stack/array:
    # 1. Pop elements from the top of the stack by removing whatever element is at the end of the array using .pop()
    # 2. Push elements to top of stack by appending them to the end of the array using .append()
    # 3. Peek at element at top of stack by looking at the last element in the array
# Not allowed to do any other operations on input array, IE: Using indexes to look at certain elements and or move
# elements around
# Solution must be recursive
# Not allowed to use any other sort of data structure

# Example
sample_array = [-5, 2, -2, 4, 3, 1]

# Answer
# [-5, -2, 1, 2, 3, 4]

# Optimal Space & Time Complexity:
# O(n^2) time (Because could potentially pop off every element from the stack whenever putting one
# in its correct place. Have to call the sort function n times and in each call could do up to n work. N * N = n^2)
# O(n) space (Because recursive call stack could at worst be of size n at a given time)
# n = length of input array

# Explanation:
# Few things to realize before continuing,
# 1. That you won't have any idea where each integer should go until the stack is completely empty.
# 2. An empty stack is also an ordered stack technically
# 3. The best way to go about this is to pop off each element until there is a sorted stack and add and pop the
#    elements off accordingly as you.

# IE:
# sample_array = [-5, 2, -2, 4, 3, 1] = stack = [1, 3, 4, -2, 2, -5]
# Pop the 1 off the stack to get
# stack = [3, 4, -2, 2, -5]
# Pop the 3 off the stack to get
# stack = [4, -2, 2, -5]
# Pop the 4 off the stack to get
# stack = [-2, 2, -5]
# Pop the -2 off the stack to get
# stack = [2, -5]
# Pop the 2 off the stack to get
# stack = [-5]
# Pop the -5 off the stack to get
# stack = []
# Stack is now empty which means it's ordered, and our call stack would look something like this -5, 2, -2, 4, 3, 1
# Now begin to add the elements back starting with element at top of call stack, -5
# stack = [-5], call_stack = 2, -2, 4, 3, 1
# Still in order since only 1 element so keep going, now with 2
# 2 > -5 so makes sense, can add to stack
# stack = [2, -5], call_stack = -2, 4, 3, 1
# Keep going with following element on call stack, -2

# *************************************************************
# -2 < 2, means not in order so instead of adding -2 to stack, pop 2 off of it to get
# stack = [-5], now compare the previous value to it to see if it's the right order
# -2 > -5, True so can add it to the stack
# stack = [-2, -5], call_stack = 2, 4, 3, 1
# *************************************************************

# Keep going with following element on call stack, 2
# 2 > -2, True so can add to stack
# stack = [2, -2, -5], call_stack = 4, 3, 1
# Keep going with following element on call stack, 4
# 4 > 2, True so can add to stack
# stack = [4, 2, -2, -5], call_stack = 3, 1
# Keep going with following element on call stack, 3

# *************************************************************
# 3 < 4, less than value at top of stack so means out of order, instead pop 4 from stack to get
# stack = [2, -2, -5], compare 3 to new top of stack
# 3 > 2, True so can add to stack to get
# stack = [3, 2, -2, -5], call_stack = 4, 1
# *************************************************************

# Keep going with following element on call stack, 4
# 4 > 3, True so can add to stack to get
# stack = [4, 3, 2, -2, -5], call_stack = 1
# Keep going with following element on call stack, 1

# *************************************************************
# 1 < 4, less than so means out of order. Instead, pop value off stack and compare to new top stack value
# stack = [3, 2, -2, -5]
# 1 < 3, still less than so keep popping stack and comparing to new top of stack
# stack = [2, -2, -5]
# 1 < 2, still less than so keep popping stack and comparing to new top of stack
# stack = [-2, -5]
# 1 > -2, True so can finally add to stack
# stack = [1, -2, -5], call_stack = 2, 3, 4
# *************************************************************

# Can now repeat process to add remaining values to stack
# 2 > 1, True so add to stack
# stack = [2, 1, -2, -5], call_stack = 3, 4
# 3 > 2, True so add to stack
# stack = [3, 2, 1, -2, -5], call_stack = 4
# 4 > 3, True so add to stack
# stack = [4, 3, 2, 1, -2, -5], call_stack = []
# Finally finished with sorted stack, not very optimal given could potentially have to pop off the entire stack every
# time something needs to be added in the correct place, but is the main idea behind answer.


# Implementation:
def sorted_stack_in_place(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sorted_stack_in_place(stack)

    insert_in_order(stack, top)

    return stack


def insert_in_order(stack, value):
    # Check to see if the stack is empty or if the value passed in is greater than element at top of stack
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        # If so, can append to top of stack
        stack.append(value)
        return

    # In case where value passed in is less than element at top of stack, pop the top element off the stack
    top = stack.pop()

    # Make a recursive call to insert again, with the still previous value that was less than the previously popped
    # stack element
    insert_in_order(stack, value)

    # Insert the popped element from before that was greater than the passed in value to the top of stack. Since we
    # know this element is greater than the value passed in, can add it to top and still be in order.
    stack.append(top)

# Example again, now with recursive call stack:
# Using same sample data of sample_array = [-5, 2, -2, 4, 3, 1]

# Would start by doing sorted_stack_in_place(stack)
# Would pop top value of stack off, top = 1
# Would call sorted again, sorted(stack)
# Repeat till array is empty
# sorted(stack), top = 3
# sorted(stack), top = 4
# sorted(stack), top = -2
# sorted(stack), top = 2
# sorted(stack), top = -5

# *************************************
# sorted(stack), no top because stack is now empty meaning base case is hit and can return empty stack
# *************************************
# Back at sorted(stack), top = -5, becomes insert_in_order(stack, -5) (The stack is empty here)
# *************************************

# insert_in_order(stack, -5), stack is empty so one of the base cases is hit
# stack.append(-5), stack = [-5], return
# Back at sorted(stack), top = 2, becomes insert_in_order(stack, 2)
# insert(stack, 2), 2 > -5 is True so can append to stack.
# stack.append(2), stack = [-5, 2]
# Back at, sorted(stack), top = -2, becomes insert_in_order(stack, -2)
# *************************************
# insert_in_order(stack, -2), -2 < 2, 2 is greater than -2 so means not in order, bypass if check and pop stack
# top = 2, stack = [-5], call insert function again, now with old value
# insert_in_order(stack, -2), -2 > -5, True so can append to stack, stack = [-5, -2], return
# Back at, top = 2, stack = [-5, -2] now, finished insert call from before so now at end of insert function
# stack.append(2), stack = [-5, -2, 2]
# *************************************
# Back at, sorted(stack), top = 4, stack = [-5, -2, 2]
# insert(stack, 4), 4 > 2, True so can append to stack, stack = [-5, -2, 2, 4]
# Back at, sorted(stack), top = 3
# insert(stack, 3), 3 < 4, 3 is less than top of stack so pop top of stack off,
# top = 4, insert(stack, 3), stack = [-5, -2, 2]
# 3 > 2, True so can append to stack, stack = [-5, -2, 2, 3]
# stack.append(top) --> stack.append(4), stack = [-5, -2, 2, 3, 4]

# *************************************
# Back at sorted(stack, 1), becomes insert(stack, 1)
# 1 < 4, 1 is less than top of stack so pop top of stack and try to insert again
# top = 4, insert(stack, 1), stack = [-5, -2, 2, 3]
# 1 < 3, still less than so keep popping,
# top = 3, insert(stack, 1), stack = [-5, -2, 2]
# 1 < 2, still less than so keep popping
# top = 2, insert(stack, 1), stack = [-5, -2]
# 1 > -2, True so insert to stack, stack = [-5, -2, 1]
# stack.append(top) = stack.append(2) --> stack = [-5, -2, 1, 2]
# stack.append(top) = stack.append(3) --> stack = [-5, -2, 1, 2, 3]
# stack.append(top) = stack.append(4) --> stack = [-5, -2, 1, 2, 3, 4]
# *************************************
# Finished


print(sorted_stack_in_place(sample_array))