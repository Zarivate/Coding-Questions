# Question
# Write a function that returns a boolean representing whether a string made up of brackets (IE: (, [, {, ), ], })
# is balanced or not.

# Note:
# A string is said to be balanced when it has an equal number of opening and closing brackets
# No brackets can be left unmatched
# An opening bracket can't match a corresponding closing bracket that came before it
# Inversely, a closing bracket can't match a corresponding opening bracket that comes after it
# Brackets can't overlap each other either, IE: [(])

# Example:
sample_string = "([])(){}(())()()"

# Answer:
# True (Because has an equal number of opening and closing brackets) In total has 6 full parentheses, 1 {}, and 1 []

# Optimal Space & Time Complexity:
# O(n) time (Will have to iterate through string once)
# O(n) space (Worst case would be having a string that is nothing but opening brackets (IE: (, [, { ) that would result
# in the entire string being in the stack)

# Explanation:
# Since stacks follow last in first out (LIFO), can utilize a stack to hold any opening brackets that might be found
# within the string as you iterate through it. If a closing bracket it ever found as you iterate through it, can check
# to see if the top of the stack has a matching opening bracket, if so means can continue iterating through the string
# otherwise if no match is found, means string is unbalanced and can return false.

# In depth example:
# sample_string = "([])(){}(())()()"
# Iterate through string and begin filling up stack until find closing bracket
# stack = [ (  ] at index 0 in string
# stack = [ (, [  ] at index 1 in string
# at index 2 in string = ], closing bracket so look if stack has matching opening bracket, stack does so can pop top
# of stack off and keep iterating through string. stack = [ (, ] now
# at index 3 in string = ), closing bracket so look if stack has matching opening bracket, stack does so can pop top
# # of stack off and keep iterating through string. stack = [ ] now
# stack = [ ( ], at index 4

# Process repeats until at end of string, if stack has anything left in it then that means string was unbalanced
# and can return False. Else if stack is empty, means all matches were found. Will have to keep eye out for possible
# edge cases however,
# IE:
# Stack is empty but find a closing bracket, means is unbalanced and can return False
# Stack isn't empty, find a closing bracket, matching opening bracket isn't at top of stack, can return False


# Implementation:
def balanced_brackets(string):
    # Set up string to hold all the potential possible opening bracket types
    opening_bracks = "([{"
    # Same idea for closing brackets
    closing_bracks = ")]}"
    #
    matching_bracks = {")": "(", "]": "[", "}": "{"}
    # Declare stack to hold brackets for later
    stack = []
    # Iterate through every character in the string
    for char in string:
        # If the character is an opening bracket, add it to the stack
        if char in opening_bracks:
            stack.append(char)
        # Else if the character is a closing bracket,
        elif char in closing_bracks:
            # If the stack is empty, means it's missing an opening bracket and can return False
            if len(stack) == 0:
                return False
            # Else, check if the last value/most recent addition in the stack is a matching bracket
            if stack[-1] == matching_bracks[char]:
                # If so, pop the item/bracket off the stack
                stack.pop()
            # Otherwise isn't a matching bracket so can return false
            else:
                return False
    # Check to see if the stack is empty, if so means string is balanced otherwise will return False
    return len(stack) == 0


print(balanced_brackets(sample_string))