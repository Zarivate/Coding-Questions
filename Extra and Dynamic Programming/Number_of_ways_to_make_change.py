# Question

# Given an array of distinct positive integers representing coins and a single non-negative integer "n",
# that represents a target amount of money, write a function that returns the # of ways to make change for that
# target given the coins provided.

# Note:
# Each coin at your disposal has an unlimited amount of uses

# Example
n = 6
example_coins = [1, 5]

# Answer:
# 2, 1 penny and 1 nickel make 1 + 5 = 6 is one solution, and 6 pennies is the other

n_2 = 10
example_coins2 = [1, 5, 10, 25]

# Answer:
# 4


# Explanation:
# Using the basis that the only way to make a value of 0 from any given amount of coins is 1, by not 
# using any coins at all, an array can be used to hold the values or the number of ways a given coin 
# can make that value. IE: Every position in the array will correlate to an amount, and that position's
# value will hold the number of ways it's position can be reached using the given coins


# Using the example values, n = 6 and coins = [1, 5]
# Create an array that goes until n + 1 (so that n is included in the array as well),
# answer_array = [_, _, _, _, _, _, _]
# Fill all the values with 0, except for the first value which will hold 1
# answer_array = [1, 0, 0, 0, 0, 0, 0]

# Then using the given coin values, iterate through the array and see how, if at all, the coin
# can reach that position value, IE:

# coin = 1, amount = 1 (because starting at the 1st position in the answer_array)
# Can a penny create the value of 1?
# Yes, so update that position from 0 to 1, but by adding the current value in that position alongside
# the one held within the position in the array from the amount - coin, IE:

# ***************************************************************************************************************
# answer_array[amount] += answer_array[amount - coin]
# answer_array[1] += answer_array[1 - 1]
# answer_array[1] += answer_array[0]
# 0 += 1
# 1
# answer_array[1] = 1
# This can be done because, thinking about it logically, if you have something like a $5 goal, and you only have $1 
# and $5 coins, and you already finished off the $1 coins, so you know there's already 1 way to make $5 which
# is with 5 $1 coins, and you move onto the $5 coin, you would automatically know intuitively that 1 $5 coin makes
# $5 thus your answer would be 2, but you could also use the knowledge of, if you removed the current coin you have
# from your goal, you'd be left wondering how you could make $0 from the coins. Because a new goal of 0 can be 
# achieved from subtracting the current coin from the goal, means previous answers can be used to get new answers.
# A more in depth explanation is given later.
# ***************************************************************************************************************

# Keep going with this approach, see if it's possible to reach the rest of the amounts in the array range
# using the current coin to get this

# answer_array = [1, 1, 1, 1, 1, 1, 1] 
# Because a $1 coin can be used to reach all these values


# Move onto the next coin, the 5
# ***************************************************************
# Can immediately skip to the 5th position in the array/amount = 5 because it's impossible for a $5 coin
# to make any value that's less than 5, so would continue from 

# coin = 5, amount = 5 (answer_array[5])
# answer_array[5] += answer_array[5 - 5] --> answer_array[0]
# 1 += 1
# 2

# answer_array = [1, 1, 1, 1, 1, 2, 1] 

# Keep going
# coin = 5, amount = 6 (answer_array[6])
# answer_array[6] += answer_array[6 - 5] --> answer_array[1]
# 1 += 1
# 2

# Can now return 2 as the answer


# Optimal Space & Time Complexity:
# O(nd) time || O(n) space
# n = target value
# d = number of types of coin

# Breakdown:
# Space
# O(n) from creating an array of size n + 1

# Time:
# O(nd)
# O(n) from iterating through the array
# O(d) from each type of coin needing its own iteration through the array
# O(nd) when put together


# Implementation:
def ways_to_make_change(n, denoms):

    # Create an array up to size n + 1, so that way n is included in the array, and initialize with all 0s
    ways = [0 for amount in range(n+ 1)]

    # Set the first position to be equal to 0, as only 1 way to make a 0 value
    ways[0] = 1

    # For loop to check every coin in the denoms array
    for coin in denoms:

        # Loop through every amount, starting from the coin and go until n + 1 (n is included this way)        
        for amount in range(coin, n + 1):
            
            # Set the value in the array to be equal to be whatever value is already there plus the value in the
            # ways array at the current amount - current coin
            ways[amount] += ways[amount - coin]

    # Return the nth position in the array for an answer
    return ways[n]


print()
print("The number of ways to make change for " + str(n) + 
      " and the coins " + str(example_coins) + " is " + 
      str(ways_to_make_change(n, example_coins)))
print()

print()
print("The number of ways to make change for " + str(n_2) + 
      " and the coins " + str(example_coins2) + " is " + 
      str(ways_to_make_change(n_2, example_coins2)))
print()

