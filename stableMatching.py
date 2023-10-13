# Question:

# Given two 2 dimensional lists, one that represents interns preference ranking of teams they could be assigned to, and
# another list that represents the teams and their ranking for which interns they'd prefered to have on their teams. Find
# the best possible combinations for the interns and teams. The function should return a 2 dimensional list representing
# this combination. The returning list doesn't have to be in any specific order.

# Notes:
# List will always be of length N, with integers as their elements
# 1 intern can be assigned to 1 team only and vice versa
# Each pairing should be "stable", meaning that there are no matches where both teams and interns would prefer to be with others
# In cases where there are multiple solutions, solution most optimal for intern's preferences should be given


# Example:
example_interns = [
    [0, 1, 2], # Intern 0 prefers teams 0 > 1 > 2
    [1, 0, 2], # Intern 1 prefers teams 1 > 0 > 2
    [1, 2, 0]  # Intern 2 prefers teams 1 > 2 > 0
]

example_teams = [
    [2, 1, 0], # Team 0 prefers intern 2 > 1 > 0
    [1, 2, 0], # Team 1 prefers intern 1 > 2 > 0
    [0, 2, 1]  # Team 2 prefers intern 0 > 2 > 1
]

# Answer: There are multiple solutions for this problem so the most optimal pairings in favor of the interns is given
optimal_groups = [
    [0, 0], # Intern 0 with team 0
    [1, 1], # Intern 1 with team 1
    [2, 2]  # Intern 2 with team 2
]


# Explanation:
# Intern 0's prefered team was 0, even though that team had intern 0 as their last choice
# Intern 1's prefered team was 1, team 1 also had intern 1 as their prefered choice so match was a given
# Intern 2's prefered team was 1, however team 1 has intern 2 as their 2nd choice and was already taken, so was left with team 2

# From a conceptual standpoint, the way the solution would breakdown is by first giving each intern their first choice,
# then any conflicts are resolved by having the teams's preference decide which intern gets to go on which team. IE:

# At first the pairings will be like so
# Intern 0
# [0, 0]
# Intern 1
# [1, 1]
# Intern 2
# [2, 1]

# There is a conflict for who gets to go on the first team, as both interns 1 and 2 want to be on it. So instead we go to see which
# intern team 1 prefers, they prefer 1 > 2 > 0, so it is given to intern 1 as that is team 1's first choice. Which leaves the 2nd 
# intern with the 2nd team. Who while have intern 2 as their 2nd choice, is still the most optimal groupings in favor of the interns.


# Code wise, certain things will need to be tracked, among these being
# Intern being chosen
# Intern choices
# Any interns still needing to be chosen/interns having to rechoose if their first choice isn't optimal
# Team's rankings of interns when conflicts arise

# In order to avoid having to iterate over each team whenever a conflict arises, a map of each team's rankings 
# will be used. The map will consist of something like
# {intern: rank}, like so

# team_intern_rankings = [
#   {2: 0, 1: 1, 0: 2},
#   {1: 0, 2: 1, 0: 2},
#   {0: 0, 2: 1, 1: 2},
# ]

# Where the intern is the key and the value is their rank

# Implementation:


# Time & Space Complexity:
# O(n^2) time
# O(n^2) space
# n = number of interns

# Time Breakdown:
# At worst, each intern "n" will have to go through every team "n", "n" can be used for both the interns and teams here
# because there are the same amount of each.
# The Maps generated to keep track of choices results in having to go through every team and every intern preference for
# each team, resulting in n^2 as well. 

# Space Breakdown:
# The extra space mainly comes from the map made to know each team's rankings of interns, which would be the same length as
# the number of teams, "n", and in each team entry they would have an entry for every intern "n". Resulting in n^2 space.

# There's also some extra space used for keeping track of the other things like which intern still needs to be assigned, the
# returning answer list, etc, but all those are O(n) space so are dwarfed by the map space used.


# Implementation:
def stablePairs(interns, teams):
    # Dictionary to hold pairings
    pairs = {}
    # List of possible interns that could be left, any one of them could be left so is same length as interns, IE: [0, 1, 2]
    internsLeft = list(range(len(interns)))
    # Since each intern could go through every team before finding their ideal one, an array all starting at team 0 is used that 
    # will progressively be incremented to represent a new team, IE: [0, 0, 0], but if intern 2 isn't fit for team 0, it will be 
    # incremented like so [0, 0, 1] and [0, 0, 2].
    currInternChoices = [0] * len(interns)

    teamMaps = []
    # n^2 time done here, nested for loop, for each team each intern is looped through
    for team in teams:
        rank = {}
        # Find the internRank and their number within the current team
        for internRank, internNum in enumerate(team):
            # Set their ranking
            rank[internNum] = internRank
        # Add it to the team intern collection
        teamMaps.append(rank)

    # So long as interns still need team assignment
    while len(internsLeft) > 0:
        # Grab an intern
        internNum = internsLeft.pop()

        # Find that specific intern within the interns, will hold their team rankings
        intern = interns[internNum]
        # Find that intern's first team choice
        firstChoice = intern[currInternChoices[internNum]]
        # Increment that intern's choice by 1, to show has gone past their first choice now
        currInternChoices[internNum] += 1

        # If the intern's first choice is open
        if firstChoice not in pairs:
            # Join that team with that intern
            pairs[firstChoice] = internNum
            # Iterate the while loop again
            continue

        # Else if it's not open, means another intern is assigned to that team so find that previous intern
        previousIntern = pairs[firstChoice]
        # See what their ranking is
        previousInternRank = teamMaps[firstChoice][previousIntern]
        # See what the ranking is of the intern trying to take their spot
        currInternRank = teamMaps[firstChoice][internNum]

        # If the intern trying to replace the previous one is prefered by the team
        if currInternRank < previousInternRank:
            # Add the previous intern to the interns that still need a team
            internsLeft.append(previousIntern)
            # Pair the team up with the intern replacing the old one
            pairs[firstChoice] = internNum
        else:
            # If that's not the case add the intern trying to replace the old one to the interns that still need a team
            internsLeft.append(internNum)

    # Because the pairs dictionary is in reverse order from what the answer wants, is just returned as and array but in reverse order
    return [[intern, team] for team, intern in pairs.items()]


# Example result
print(stablePairs(example_interns, example_teams))