# Question

# Write a function that takes in a non-empty list of strings and returns a list of characters that are common in
# all the strings, ignoring any multiple cases. IE: Multiple instances of the same letter in a string.

# Note:
# Strings could have more than just alphanumeric characters
# Returned list can be in any order

# Example:
example_strings = ['1be', 'b2e', '4baeed']


# Answer (Could be in a different order)
# ['b', 'e']

# Optimal Space & Time Complexity:
# O(n * m) time
# O(m) space
# n = number of strings
# m = length of the longest string

# Explanation:
# Main idea is to realize that whichever string is the shortest, will determine which characters can be returned
# as an answer. IE: The shortest string's characters must be in all the other strings.
# 1be and b2e in example are same length but just use the first one as an example, in solution will need to find
# the shortest string first by iterating through all the strings 1 time beforehand
# Convert the first string into a set with its characters
# potential_matches = { '1', 'b', 'e'}
# Now iterate through these matches and see if the rest of the strings have all the characters, any not found
# are removed from the potential matches, IE:
# b2e, have 'b' and 'e' but not '1' so
# potential_matches = {'b', 'e'}
# 4baeed, have 'b' and 'e' so
# potential_matches = {'b', 'e'}
# Now just convert potential_matches to an array and return for result
# answer = ['b', 'e']

# The space and time complexity would break down like this for the solution
# Time
# O(n) to iterate through all the strings once to find the shortest string
# O(n) again to iterate through the strings once more to compare with potential matches
# O(m) to convert each string into a set
# finally iterate through potential matches at each string

# Space
# O(m) because of how any non-current sets would be garbage collected, meaning the space would only reach up to the
# length of the longest string

# Implementation:
def common_characters(strings):
    # Call function to find the shortest string
    shortest_string = get_shortest(strings)
    # Set the potential matches to be the unique characters in the shortest string, is a set in order to avoid
    # any duplicates
    potential_matches = set(shortest_string)

    # Iterate through strings while removing any characters from potential matches that are missing in the other strings
    for string in strings:
        remove(string, potential_matches)

    # Return remaining list of matches
    return list(potential_matches)


# Function to find the shortest string
def get_shortest(strings):
    shortest_string = strings[0]
    for string in strings:
        if len(string) < len(shortest_string):
            shortest_string = string

    return shortest_string


# Function to modify existing set of potential matches
def remove(string, potential_matches):
    # Convert passed in string into a set that will hold all it's unique values
    unique_chars = set(string)

    # In order to avoid modifying set as iterating through it which could cause problems, is first converted into a
    # list
    for character in list(potential_matches):
        # If the character isn't in potential matches, it is removed
        if character not in unique_chars:
            potential_matches.remove(character)


print(common_characters(example_strings))