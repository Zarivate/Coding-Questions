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

# A more visual way to see the example is

# City 1, distances[0] and fuel[0] -> 5 miles to get to city 2 but can get 1 gallon of gas here
# City 2, distances[1] and fuel[1]
# City 3, distances[2] and fuel[2]
# City 4, distances[3] and fuel[3]
# City 5, distances[4] and fuel[4]

