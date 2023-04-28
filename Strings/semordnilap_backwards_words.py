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

# **********************************************************
# Because length of words not limited to something like the letters of the English alphabet and can be of any size
# and use any sort of characters, can't reduce time and space complexity to O(n).
# **********************************************************

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
def semordnilap(words):
    # Create a set from the given words
    set_words = set(words)
    # Create an array to hold future pairs
    answers = []

    # Iterate through the words
    for word in words:
        # Reverse each word and hold within a variable to compare for later
        reverse = word[::-1]
        # Check to see if the reverse exists within the Set and that the reverse isn't the same as the normal word,
        # since that would just be a palindrome, not a semordnilap
        if reverse in set_words and reverse != word:
            # Add pair to answer array
            answers.append([word, reverse])
            # Remove the pair from the Set
            set_words.remove(word)
            set_words.remove(reverse)

    return answers


print(semordnilap(sample_words))


# Bonus slightly cleaner version: No need to remove from Set or initially populate it.
def semordnilap_cleaner(words):
    # Initialize a set
    words_set = set([])
    # Create answer array
    answers = []
    # Iterate through array
    for word in words:
        # Reverse the word and store it within a variable
        reverse = word[::-1]
        # Check if reverse word exists in set
        if reverse in words_set:
            # If so, add pair to answers array
            answers.append([word, reverse])
        # Else if word doesn't exist in Set yet, just add it to the Set
        words_set.add(word)

    return answers


print(semordnilap_cleaner(sample_words))