# Question: Greedy Algorithm

# Given 2 arrays, one representing distances between cities and another the fuel/gallons that can be obtained at those cities 
# alongside a mpg, return the starting city index that allows you to start at and travel clockwise to all the cities on the
# exact amount of fuel needed. 

# Notes:
# Can assume will always be given at least 2 cities.
# Fuel tank will always start out empty.
# Mpg will always be positive.
# Any solutions will be unique, meaning there will only be 1 possible solution to the question.
# There will always be enough gas to go around once.

# Example:

example_distances = [5, 25, 15, 10, 15]
example_fuel = [1, 2, 1, 0, 3]
example_mpg = 10

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

# The thing to notice here is to first keep track of how much gas you'll be left with at each stop by itself. In otherwords 

# City 1 --> City 2
# Takes 5 miles to get to City 2, but can get 1 gallon of gas for 10 miles of travel. In otherwords going from City 1 to City 2 will result in 5 miles left over
# Since started at first city it has 0 for it's position in the array. Since cost nothing because started there.

# [0, 5]

# City 2 --> City 3
# Takes 25 miles to get to City 3, can get 2 gallons of gas for 20 miles of travel + 5 from before to have just enough to make it.
# [0, 5. 0]

# City 3 --> City 4
# Takes 15 miles, can get 1 gallon of gas. Meaning have -5 miles for this trip since have none left over from before.
# [0, 5, 0, -5]

# City 4 --> City 5
# Takes 10 miles, can get 0 gallons of gas. So have -10 miles for this trip and then the -5 from before to get -15.
# overallTravel = [0, 5, 0, -5, -15]

# In otherwords this array represents the overall ability to travel from one city to the next. Using the knowledge that there will always be at least enough gas for 1 round trip, 
# and the knowledge that previous values bring value to the overall outcome. Can assume the value with the lowest value will be the best starting point as that is the city 
# with the most to gain. A simpler explanation is below.

# IE: 
# Something like 
# gas = [2, 3, 0]
# distances [0, 0, 50]
# overallTravel = [0, 20, 50]
# mpg = 10

# You can only go from the last point (distances[3]) to the first (distances[1]), in otherwords finish the round trip, by first going to the first 2 cities and filling up on the 
# 5 gallons of gas on the way. If you only went to 1 of the first 2 cities, then you wouldn't have enough to make it. Thus the best starting city would be the first, or
# the first position in the array.


# Implementation:
def validStart(distances, fuel, mpg):
    miles = 0
    startCity = 0
    currentMiles = 0
    
    for position in range(1, len(distances)):
        distanceFromLastCity = distances[position - 1]
        fuelFromLastCity = fuel[position - 1]
        miles += fuelFromLastCity * mpg - distanceFromLastCity

        if (miles < currentMiles):
            currentMiles = miles
            startCity = position

    return startCity


print(validStart(example_distances, example_fuel, example_mpg))


