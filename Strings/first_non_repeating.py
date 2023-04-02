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

# Implementation:
def first_non_repeating_character(string):
    char_frequencies = {}

    for character in string:
        char_frequencies[character] = char_frequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if char_frequencies[character] == 1:
            return idx
    return -1

print(first_non_repeating_character(string_sample))