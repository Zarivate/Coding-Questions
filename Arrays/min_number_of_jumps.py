# Note: Can also be considered a dynamic programming question due to how the answers are coded
# Note: Famous/common interview question

# Question:
# Given a non-empty array of positive integers, where each integer represents the maximum number of steps you can
# take forward in the array, IE: An array of [3,1,5,2,7], where the first position is "3", you can move up to 3
# positions forward in the array, up to the position with a value of "2".

# Write a function that returns the minimum number of jumps needed to reach the final index/last position in the array
# Note: Any jump/move from index "i" to index "i + x" counts as just 1 jump, no matter how big "x" is.

# Example:
# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

# Answer:
# 4 (Because can go from 3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)

