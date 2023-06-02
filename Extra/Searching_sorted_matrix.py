# Question:

# Write a function that returns an array correlating to a position in a sorted matrix (2 dimensional array) that is the
# location of a target value.

# Notes:
# If the target value is not in the matrix, return [-1, -1]
# Each row and column in the matrix is sorted
# Rows and columns can have different heights and widths


# Example:
target_example = 44
matrix_example = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]


# Answer:
# [3, 3]


# Explanation:
# The important thing to realize is that the matrix is sorted. While each row and column may be of different size,
# because they're sorted. They can be searched through rather easily. To start, will need to start at the greatest
# possible starting position and slowly work our way through the matrix to the target value.

# IE:
# Start at the end of the first row, which would also correlate to the last column in the matrix. In the example it
# would be 1000
# matrix = [
#     [1, 4, 7, 12, 15, 1000(right here)],
#     [2, 5, 19, 31, 32, 1001],
#     [3, 8, 24, 33, 35, 1002],
#     [40, 41, 42, 44, 45, 1003],
#     [99, 100, 103, 106, 128, 1004],
# ]

# Then check to see if that value is greater than, less than, or equal to the target value
# 44 < 1000, 1000 is greater and because of that can eliminate that entire column, now move back 1 position in the row

# 44 > 15, 44 is greater which means can eliminate entire left of this row, now move down 1 column and check that value

# 44 > 32, 44 is still greater so can eliminate left of this row too, move down 1 column again and check that value

# 44 > 35, 44 is still greater so eliminate left of this row and move down 1 column again

# 44 < 45, 44 is less than current value so can move left in row by 1 and check that value

# 44 = 44, have found target value so can return

# The main idea is that, using the knowledge that the matrix is sorted. If start at the greatest possible start, in this
# case being the end of the first row/last column of the first row, depending on whether the value is less than or
# greater than the target value, changes where to traverse in the matrix.

# In the cases where:

# The target is less than the current position in the matrix:
# Means can eliminate that entire column, as anything in that column will be greater than the target value. Then can
# go left by 1 position/column in the row.

# The target value is greater than the current position in the matrix:
# Means can eliminate the left of that row, as anything to the left will be less than the target value. Then can move
# down by 1 row

# Keep doing this until either find target value or realize value does not exist in matrix


# Optimal Space & Time Complexity:
# O(n + m) time
# O(1) space
# n = length of matrix rows
# m = length of matrix columns
# Because in worst case will have to search through entire row and column
# 1 space because not creating any extra space that scales with solution


# Implementation:
def search_sorted_matrix(matrix, target):
    # Set the row to be the first one
    row = 0

    # Set the column to be the last one
    column = len(matrix[0]) - 1

    # While loop to continue so long as neither the row nor column go out of bounds
    while row < len(matrix) and column >= 0:

        # If the value in the position is greater than the target
        if matrix[row][column] > target:
            # Go left/back 1 position/column
            column -= 1
        # Else if the value in the position is less than the target
        elif matrix[row][column] < target:
            # Go down 1 row
            row += 1
        # Else means have found target value and can return the position
        else:
            return [row, column]

    # If never able to find target then just return [-1, -1]
    return [-1, -1]


print(search_sorted_matrix(matrix_example, target_example))
