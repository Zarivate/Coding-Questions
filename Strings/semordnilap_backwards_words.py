# Question:

# Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

# Notes:
# A semordnilap is a word that becomes a different word when read backwards. A semordnilap pair are words that
# are a set of strings where the reverse of a word is the same as the forward of another.
# IE: "palindromes" and "semordnilap", "smug" and "gums", etc.

# Order of returned pairs and order of strings within each pair don't matter

# Example:
sample_words = ["smug", "test", "gums", "abc", "cba"]

# Answer:
# [["smug", "gums", ], ["abc", "cba"]]

# Optimal Space & Time Complexity
# O(n * m) time (O(n) for iterating through words, O(m) for reversing each word, the worst would be the longest one)
# O(n * m) space (n is from number of words added to Set, m is from upper bound of space needed for longest word)
# n = number of words
# m = length of the longest word

# Explanation:
# The main idea to realize here is, when comparing words, there is only ever 1 possible combination of the reverse of a
# word. For instance, "smug" backwards will always be "gums" and vice versa. They will never be other words you could
# compare them too and have them be the same. Conceptually, could use this info paired with a Set like data structure
# that has constant insert and lookup times alongside not allowing duplicates, to hold not just the words given,
# but also the reverse of the words. After the set is populated, could iterate through the words and see if their
# reverse exists within the Set like data structure. If it does exist, could remove pair from the Set, and return them
# in some sort of 2D answer array. Would repeat this until Set is either empty or reach end of words. IE:

# Populate Set by iterating through array once and filling it up with the word and their reverse counterpart
# set = {"smug", "test", "gums", "abc", "cba"}
# Then iterate through the words again, and check for pairs
# current_word = "smug", reverse is "gums" and does exist in Set so remove from Set, and add pair to answer array
# answer_array = ["smug", "gums"]
# set = {"test", "abc", "cba"}
# current_word = "test", reverse is "test" which doesn't exist in Set so move on
# current_word = "gums", reverse already found and no longer exists within Set so move on
# current_word = "abc", reverse is "cba", exists in Set so remove from Set, and add pair to answer array
# answer_array = [["smug", "gums"], ["abc", "cba"]]
# set = {"test"}
# Reach end of words so can return answer array

# Implementation:
