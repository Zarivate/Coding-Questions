# Question:

# Given 2 arrays, one representing distances between cities and another the fuel/gallons that can be obtained at those cities 
# alongside a mpg, return the starting city index that allows you to start at and travel all the way around the cities on the
# exact amount of fuel needed.

# Notes:
# Can assume will always be given at least 2 cities.
# Fuel tank will always start out empty.
# Mpg will always be positive.

# Example:

distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Answer:
# Output = 4

# A more visual way to see the example is by thinking of it like so
# City 1, distances[0] and fuel[0] -> 5 miles to get to City 2 but can get 1 gallon of gas
# City 2, distances[1] and fuel[1] -> 25 miles to get to City 3 but can get 2 gallons of gas
# City 3, distances[2] and fuel[2] -> 15 miles to get to City 4 but can get 1 gallon of gas
# City 4, distances[3] and fuel[3] -> 10 miles to get to City 5 but can get 0 gallons of gas
# City 5, distances[4] and fuel[4] -> 15 miles to get to City 1 but can get 3 gallona of gas

# Explanation:
# The answer would need to be city 5 or index 4 because at that point you would get 3 gallons of gas. Which means you would start of
# with 30 gallons of gas. Doing the math as you travel along the cities you would get

# Start at city 5, get 3 gallons of gas to be able to travel 30 miles
# Travel to city 1, takes 15 miles to get there, 30 - 15 = 15 miles left
#       Can get 1 gallon of gas at city 1, 15 + 10 = 25 miles
# Travel to city 2, takes 5 miles to get there, 25 - 5 = 20 miles left
#       Can get 2 gallons of gas at city 2, 20 + 20 = 40 miles
# Travel to city 3, takes 25 miles to get there, 40 - 25 = 15 miles left
#       Can get 1 gallon of gas at city 3, 15 + 10 = 25 miles
# Travel to city 4, takes 15 miles to get there, 25 - 15 = 10 miles left
#       Can get 0 gallons of gas at city 4, 10 + 0 = 10 miles
# Travel back to city 5 takes 10 miles to get there, 10 - 10 = 0 miles left

# Have now completed a round trip using up exactly how much gas was possible to get along the way

# TODO: Draw visual version of question


