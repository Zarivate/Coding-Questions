# Question:
# Write a function that takes in a string of lowercase English-alphabet letters and returns the index of
# the string's first non-repeating character. If the input string doesn't have any non-repeating characters,
# return -1.

# Note:
# First non-repeating chracter in a string is the first character that occurs only once

# Example:
string_sample = "abcdcaf"


# Answer: 1 (Because "b" was the first non-repeating character at index 1)

# Optimal Space Time Complexity:
# O(n) time
# (Because have to iterate through string at least once, if not more depending on solution implementation)

# O(1) space
# (This is because in optimal approach, that utilizes a Hashtable, it's size will always be 26/will never
# have more than 26 frequencies because that's the max number of lowercase English alphabet letters and
# O(26) rounds down to O(1).

# Explanation:
# The main idea is to use a Hashtable, iterate through the string one time to fill up the table with the
# characters and their frequencies, then go through the string again and whichever character has a value of
# 1 in the table first, return that index. Else return -1.


# Implementation:
def first_non_repeating_character(string):
    # Create a data structure that'll hold the characters and their frequencies
    char_frequencies = {}

    # Iterate through string once
    for character in string:
        # Fill up the data structure with the character alongside it's frequency
        char_frequencies[character] = char_frequencies.get(character, 0) + 1

    # Iterate through string again
    for idx in range(len(string)):
        # Get the current character in the string
        character = string[idx]
        # Check to see if it has a value of 1 in the data structure
        if char_frequencies[character] == 1:
            # If so, return its index
            return idx
    return -1


# Bonus Un-optimal Solution:

# Space & Time Complexity:
# O(n^2) time (Because at every index in the string, we would iterate through the entire string again)
# O(1) space (Because no scaling space is created)


# Implementation:
# The main idea is to have a double for loop. Where for each character in the string, you check the rest of the
# string to see if there's a matching character. This process repeats until the first non-repeating character is
# found utilizing a boolean check.

def first_non_repeating_character_unoptimal(string):
    # Outer for loop to iterate through string
    for idx in range(len(string)):
        # Boolean to decide whether a duplicate character has been found or not. Since want first non-repeating
        # character, is set to False at start and may or may not be set to True later
        found_dup = False
        # Inner for loop to iterate through string as well
        for idx2 in range(len(string)):
            # Check to see if the rest of the strings have any of the same character as the current character in the
            # outer loop.
            if string[idx] == string[idx2] and idx != idx2:
                # If a match is found, set boolean to true
                found_dup = True

        # If the boolean is false, return the index for the outer character
        if not found_dup:
            return idx
    return -1


print(first_non_repeating_character(string_sample))
print(first_non_repeating_character_unoptimal(string_sample))
