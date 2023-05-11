# Question

# Given a row of seats and a list of constraints, find the best seat to sit in. Assuming this row of seats
# is represented as an integer array, where 1s represent filled in seats and 0s represent empty seats,
# return the corresponding index.

# Notes/Constraints:
# May assume the first and last seats are always filled

# Seat must be one that gives the most space, with each side being evenly distributed. IE: In a row of 3 empty
# seats, would like to sit in the middle.

# When there are two equally good seats, return the one with a lower index

# Given array will always have a length of at least 1 and have only 0s and 1s.

# If there is no place to sit, return -1.


# Example:
seats_example = [1, 0, 1, 0, 0, 0, 1]

# Answer:
# 4 (seats_example[4] = 0, is only position that fits constraints since is between an even number of 0s to the left and
# right)


# Optimal Space & Time Complexity:
# O(n) time
# O(1) space
# n = number of seats/length of array


# Explanation:
# The main thing to realize for this problem is how the answer will be the middle position of the longest 0 subarray
# in the array. IE: In the example,

# index 4 is in the middle of the [0, 0, 0] subarray of [1, 0, 1, 0, 0, 0, 1]

# The problem comes with keeping track of this and how to properly get the corresponding index. This can be solved
# using 2 pointers, both will iterate through the array but the second pointer will do so ahead of the first. The first
# pointer won't move until a 1 is found by the second pointer, at which point the middle index of the two pointers will
# be calculated. IE:

# pointer_1 = 0
# pointer_2 = 1
# biggest_sub_size = 0
# best_seat = -1 (Value will be updated as you iterate through array)

# seats_example = [1, 0, 1, 0, 0, 0, 1]
# [1(pointer_1 here), 0(pointer_2 here), 1, 0, 0, 0, 1]
# pointer_2 = 0, is not a 1 so keep going

# [1(pointer_1 here), 0, 1(pointer_2 here), 0, 0, 0, 1]
# pointer_2 = 1 so stop and calculate size of subarray.
# biggest_sub_size = pointer_2 - pointer_1 - 1
# biggest_sub_size = 2 - 0 - 1 = 1
# Now calculate middle/best seat
# best seat = pointer_2 + pointer_1 / 2
# best seat = 2 + 0/2 = 2

# Now that have finished first subarray, move the first pointer to the same place as the second pointer and continue
# pointer_1 = 2
# pointer_2 = 2
# biggest_sub_size = 1
# best_seat = 1

# [1, 0, 1(pointer_1 here), 0(pointer_2 here), 0, 0, 1]
# Pointer 2 is equal to 0, not 1 so keep going

# [1, 0, 1(pointer_1 here), 0, 0(pointer_2 here), 0, 1]
# Pointer 2 is equal to 0, not 1 so keep going

# [1, 0, 1(pointer_1 here), 0, 0, 0(pointer_2 here), 1]
# Pointer 2 is equal to 0, not 1 so keep going

# [1, 0, 1(pointer_1 here), 0, 0, 0, 1(pointer_2 here)]
# Pointer 2 is equal to 1, so calculate size of subarray and best seat
# biggest_sub_size = 6 - 2 - 1 = 3
# best_seat = 6 + 2/2 = 4

# Now have finished second subarray, move the first pointer to the same place as the second pointer and continue
# pointer_1 = 6
# pointer_2 = 6
# biggest_sub_size = 3
# best_seat = 4

# Moving the second pointer any further would result in it being outside the array so can finish by returning the
# best seat variable for an answer.


# Space & Time Complexity breakdown:
# Time:
# O(n) when iterating through array at least 1 time

# Space
# O(1) because no scaling space is created for the solution, only some simple variables


# Implementation:
def bestSeat(seats):
    best = -1
    biggest_subarray = 0

    pointer_1 = 0

    while pointer_1 < len(seats):
        pointer_2 = pointer_1 + 1
        while pointer_2 < len(seats) and seats[pointer_2] == 0:
            pointer_2 += 1

        current_sub_size = pointer_2 - pointer_1 - 1
        if current_sub_size > biggest_subarray:
            best = (pointer_1 + pointer_2) // 2
            biggest_subarray = current_sub_size
        pointer_1 = pointer_2

    return best


print(bestSeat(seats_example))
