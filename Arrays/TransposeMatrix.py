# Question:

# Given a 2D Array of integers, write a function that returns the transpose of it.

# Notes:
# Width and height of matrix can be different
# Can assume input matrix will always have atleast 1 value

# Example:

example_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Answer: 
# [
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ]


# Optimal Space & Time Complexity:
# O(n) space | O(n) time (Can also be seen as O(w*h) where w=width and h=height of input matrix)
# n = number of elements in input matrix


# Explanation
# This is a rather simple problem once you figure out the pattern. That being how the transpose of a matrix is just the flipped version of
# the original matrix across it's diagonal. Which is why the position of the 1, 5, and 9 don't change in the answer matrix. But the positions
# of all the values on both sides of that line do get flipped. IE: In the example matix, the 2 and 4 swap places, the 3 and 7 swap places,
# and the 8 and 6 swap. Using this, you can use the positions of the columns integers to decide where to re-place the values.
# IE:

# Column 0 in the example matrix consists of 1, 4, 7, which equates to the first row in the answer matrix. Column 1 in the example matrix is
# [2, 5, 8] which is equal to row 1 in the answer matrix and so forth. The same is true about the rows and even in situations where the number
# of rows and columns are not the same. However when iterating through, you have to be careful to not confuse the rows and columns else the
# matrix will come out wrong.

example_matrix2 = [
    [1,2],
    [4,5],
    [7,8]
]

# Answer: 
# [
#     [1,4,7],
#     [2,5,8],
# ]

# The example above has 2 columns but 3 rows, however the resulting transpose has 3 columns and 2 rows. Meaning so long as you keep track of the column
# values when creating the new rows for the transpose matrix, you can easily find the solution.


# Implementation:
def transposeMatrix(matrix):
    transposed_Matrix = []

    # Iterate through every column in the matrix
    for column in range(len(matrix[0])):
        # Create an array that will store the new row for the transposed Matrix 
        transposed_row = []
        # Iterate through every row in that column
        for row in range(len(matrix)):
            # Append the value to the new transposed row
            transposed_row.append(matrix[row][column])
        # Append the newly created row to the transposed Matrix
        transposed_Matrix.append(transposed_row)

    return transposed_Matrix


print(transposeMatrix(example_matrix))
print(transposeMatrix(example_matrix2))












