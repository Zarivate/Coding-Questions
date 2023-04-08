# Question
# Write a function that returns a boolean representing whether a string made up of brackets (IE: (, [, {, ), ], })
# is balanced or not.

# Note:
# A string is said to be balanced when it has an equal number of opening and closing brackets

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
# within the string as you iterate through it. If you ever come across a 


# Implementation:
def balanced_brackets(string):
    opening_bracks = "([{"
    closing_bracks = ")]}"
    matching_bracks = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in opening_bracks:
            stack.append(char)
        elif char in closing_bracks:
            if len(stack) == 0:
                return False
            if stack[-1] == matching_bracks[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(balanced_brackets(sample_string))