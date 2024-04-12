# Question:

# A pseudo sequel to the number of ways to make change question, in this question you're also given an array of positive
# integers representing coin values and a single non-negative integer "n" representing a target value. Write a function
# that returns the smallest number of coins needed to make change for the target "n"

# Notes:
# Each coin denomination allows for an unlimited number of uses for that coin
# If not possible to reach target "n" from given coins, return -1

# Example:
n = 7
example_coins = [1, 5, 10]

# Answer:
# 3 (2 pennies and 1 nickel)

n_2 = 6
example_coins2 = [1, 2, 4]


# Answer:
# 2 (One 2 coin and one 4 coin)

# Explanation:
# Similar to how the number of ways to make change question, this problem will also utilize an array of size n+1, so n
# can be included in the array, but this time each position will hold the minimum number of coins needed to reach that
# position. IE:

# min_coins = array of size n+1, each initialized with infinity for later comparisons
# The first position in this array, 0th position, will be 0 this time instead of 1 because of how the minimum coins
# needed to make 0 would be 0.

# Afterwards, take each coin and compare it to each position in the array, if the coin is less than or equal to that
# position, then change the value in that position of the array to be equal to the minimum between either the current
# value in that position, or the position calculated from subtracting the current position and current coin + 1, IE:

# (n2 and example_coins1 are used for this breakdown)
# coin = 1, amount/position = 1
# min_coins = [0, inf, inf, inf, inf, inf, inf]
# positions =  0   1    2    3    4    5    6

# min(min_coins[amount], min_coins[amount - coin] + 1)
# min(min_coins[1], min_coins[1 - 1] + 1)
# min(inf, min_coins[0] + 1)
# min(inf, 0 + 1)
# min(inf, 1)
# 1 < inf, so place 1 in that position of the array

# min_coins = [0, 1, inf, inf, inf, inf, inf]
# positions =  0  1   2    3    4    5    6

# *************************************************************
# The intuition here is that because each position in the array holds the minimum number of coins needed to reach that
# position, by calculating which position we end up at from subtracting the current coin from the position, we
# essentially find out that we just need 1 more of the current coin from the calculated position to reach the current
# position in the array. Which is where the + 1 comes from.
# IE: If we know that it takes 10 pennies to make 10, then when we get to a nicked, we subtract 5 from 10 to get 5,
# at the 5 we see that it takes 5 pennies to get to 5, but with 5 pennies and 1 nickel we can get to 10. This would
# mean we only use 6 coins instead of the expected 10.
# *************************************************************

# keep going for the rest of the positions with the 1 coin to see you'll end up with
# min_coins = [0, 1, 2, 3, 4, 5, 6]
# positions =  0  1  2  3  4  5  6

# Then move onto the next coin, the 2
# *************************************************************
# Can skip checking until get to 2nd position cause not possible to get a 0 or 1 from a 2 coin.

# coin = 2, amount/position = 2
# min(min_coins[amount], min_coins[amount - coin] + 1)
# min(min_coins[2], min_coins[2 - 2] + 1)
# min(2, min_coins[0] + 1)
# min(2, 0 + 1)
# min(2, 1)
# 1 < 2, so place 1 in that position of the array

# min_coins = [0, 1, 1, 3, 4, 5, 6]
# positions =  0  1  2  3  4  5  6

# keep going
# coin = 2, amount/position = 3
# min(min_coins[3], min_coins[3 - 2] + 1)
# min(3, min_coins[1] + 1)
# min(3, 1 + 1)
# min(3, 2)
# 2 < 3, so place 2 in that position of the array

# min_coins = [0, 1, 1, 2, 4, 5, 6]
# positions =  0  1  2  3  4  5  6

# keep going
# coin = 2, amount/position = 4
# min(min_coins[4], min_coins[4 - 2] + 1)
# min(4, min_coins[2] + 1)
# min(4, 1 + 1)
# min(4, 2)
# 2 < 4, so place 2 in that position of the array

# min_coins = [0, 1, 1, 2, 2, 5, 6]
# positions =  0  1  2  3  4  5  6

# keep going
# coin = 2, amount/position = 5
# min(min_coins[5], min_coins[5 - 2] + 1)
# min(5, min_coins[3] + 1)
# min(5, 2 + 1)
# min(5, 3)
# 3 < 5, so place 3 in that position of the array

# min_coins = [0, 1, 1, 2, 2, 3, 6]
# positions =  0  1  2  3  4  5  6

# keep going
# coin = 2, amount/position = 6
# min(min_coins[6], min_coins[6 - 2] + 1)
# min(6, min_coins[4] + 1)
# min(6, 2 + 1)
# min(6, 3)
# 3 < 6, so place 3 in that position of the array

# min_coins = [0, 1, 1, 2, 2, 3, 3]
# positions =  0  1  2  3  4  5  6


# Same idea but now with the next coin, 4, go until finish off array to get
# min_coins = [0, 1, 1, 2, 1, 2, 2]
# positions =  0  1  2  3  4  5  6

# Now just return the "n" position in the min_coins array for an answer, so long as isn't still "inf" in which case
# just do conditional check to return -1 if that's the case.



# Optimal Space & Time Complexity:
# O(nd) time
# O(n) space
# n = target value
# d = number of coins/denominators in denoms array

# Breakdown:
# Space:
# O(n) from creation of array of up to and including "n" size

# Time:
# O(n) from iterating through array up until the "n" amount which could be the whole array in worst case
# O(d) from iterating through the denoms array
# O(nd) from possibly iterating through the entire min_coins array at each "d" in the denom array

# Implementation:
def min_coins(n, denoms):
    # Create an array up to size n + 1, so that way n is included in the array, and initialize with "inf"
    num_coins = [float("inf") for amount in range(n + 1)]

    # Set the first value to be equal to 0
    num_coins[0] = 0

    # For loop to iterate through every coin in the denoms array
    for coin in denoms:

        # For loop to iterate through every position in the num_coins array starting from the value of the coin
        for amount in range(coin, len(num_coins)):

            # Set the current value in that position of the array to be the minimum between what's already there
            # or the value in the position derived from subtracting the current coin from the current position + 1
            num_coins[amount] = min(num_coins[amount], num_coins[amount - coin] + 1)

    # Return the "n" value in the array so long as it's not still "inf", in the case it is then return -1
    return num_coins[n] if num_coins[n] != float("inf") else -1


print(min_coins(n, example_coins))
print(min_coins(n_2, example_coins2))
