# Question:

# Write a function that takes in a positive integer "digits" and a string "number" representing another
# positive integer. Remove "digits" from the string so that the number represented by the string is as large as
# possible afterwards.

# Notes:
# Order of remaining digits in "number" can't be changed
# Can assume "digits" will always be less than length of "number" and greater than 0

# Example:
number_example = "462839"
digits_example = 2

# Answer:
# 6839 (The 4 and 2 were removed)

# Optimal Space & Time Complexity:
# O(n) time (Because no matter what, will iterate through string at least once)
# O(n) space (Because at worst case stack will be of length "n", case where string is in ascending order)
# n = length of string number

# Explanation:
# What's important to realize is that no matter how large the given number is, the greatest/ most important values
# directly correspond to their positions. IE: In the sample number "462839", the beginning digits being changed also
# correspond to the biggest gain/loss a number can have. IE: Changing the first digit "4" into 5, 6, 7, 8, or 9 will
# make the number hundreds of thousands greater. Using this info, no matter how many digits will need to be removed.
# The goal should be to keep the largest possible digits in the front to get the greatest possible value.

# Conceptually would work like this, iterate through the number string first,
# number_example = "462839"
# digits_example = 2
# Start at the first digit in the number, 4
# Move onto the next digit, 6, notice that it's greater than 4 and would want the 6 to be in front, not the 4
# Remove the 4, decrement the digit value by 1
# new_number = "6"
# digits_example = 1
# Move onto next digit, 2, less than new number in front, 6, so keep for now
# Move onto next digit, 8, 8 > 2, would want 8 in front of the 2 instead so,
# Remove the 2, decrement digit value by 1
# new_number = "68"
# digits_example = 0
# Removed all digits that need to be removed so can just add rest of string to new_number and return for answer
# new_number = "6839"

# ******************************************************************************************************
# Important to realize though that there could be examples where you would need to use up more than 1 digit place
# removal to get the answer.
# ******************************************************************************************************
# IE: Something like
# number_example = "648239"
# digits_example = 2
# Would need to remove both the "6" and "4", using up both digit removals in the process, to get the largest answer of
# new_number = "8239"
# Since 8 is greater than both first digits, would want it to be in the first position

# Using a stack's LIFO property, can use it to implement how the digits being removed are the most recent ones. IE:
# number_example = "648239"
# digits_example = 2
# stack = []
# Iterate through string like normal,
# current_number = 6
# stack = [6]
# current_number = 4
# 6 > 4, so no need to pop, instead just add to stack,
# stack = [6, 4]
# current_number = 8
# 8 > 4, so pop off stack and decrement digits by 1
# stack = [6]
# digits_example = 1
# 8 > 6, pop 6 off stack and decrement digits by 1
# stack = []
# digits_example = 0
# No more numbers to compare, so add to stack,
# stack = [8]
# current_number = 2
# 2 < 8, but digits_example = 0, so no need to compare really, can just add rest of string to stack.
# stack = [8239]
# Last would be to convert stack into a string and return it

# ******************************************************************************************************
# Potential edge case where number string is already in ascending order and iterate through it without popping anything
# off the stack.
# ******************************************************************************************************
# IE:
# number_example = "9876654"
# digits_example = 2
# All the numbers are in ascending order, cases where numbers are the same value wouldn't be removed either,
# IE: when reaches the second "6" wouldn't remove because removing a 6 for a 6 doesn't change anything.
# At the end the stack would just be the whole string,
# stack = [9876654]
# The answer at this point would be to remove the last 2 digits, since those numbers are at the end of the string and
# would cause the smallest lost if removed/have the least significance value wise. In other words would need to keep
# popping off the stack until no more digits left to remove, IE:
# stack = [987665]
# digits_example = 1
# stack = [98766]
# digits_example = 0
# Finally return stack as string for answer


# Implementation:
def greatest_digit_values_stack(number, digits):
    # Initialize a stack to hold values for later
    stack = []

    # Iterate through the string
    for digit in number:
        # So long as there are still digits to remove, the stack isn't empty, and the current digit is greater than
        # the value at the top of the stack.
        while digits > 0 and len(stack) > 0 and digit > stack[len(stack) - 1]:
            # Decrement digits value by 1
            digits -= 1
            # Pop top value off stack
            stack.pop()

        # Append value to stack
        stack.append(digit)

    # For cases where number string is already in ascending order and iterate through without popping anything, would
    #  simply keep popping off the end of the stack, the end of the number string, until no more digits left to pop
    while digits > 0:
        digits -= 1
        stack.pop()

    # Turn stack into string and return for answer
    return "".join(stack)

# Notes for above solution:
# Nested while loop within for loop won't affect time complexity because at most will go through the while loop
# "digit" times, where digit is always guaranteed to be positive and less than the length of the string. Same reason
# don't have to worry about the bottom while loop that removes values from the stack. As at most would go up
# until "digit" times.

# To transform and return the stack as a string will also be an O(n) operation, because of how Big O notation works
# however, something like O(2n) is reduced to O(n)


print(greatest_digit_values_stack(number_example, digits_example))