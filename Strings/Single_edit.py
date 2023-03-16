# Question:
# Given two strings, write a function that returns a boolean that determines if they can be
# made the same in only 1 edit. For this question, there are only 3 possible types of edits

# 1. Replace: A character in one string is swapped for a different character
# 2. Add: A character is added at any index in one of the strings
# 3. Remove: A character is removed at any index in one of the strings

# Note: Both strings will have at least 1 character, if strings are the exact same and or can be made the same
# return true, else false.
# Note: The Add and Remove options are essentially the same since they can both be used to make two strings the same.
# IE: "Hwdy" and "Howdy", could be make the same by either adding or removing "o"

# Example:
# stringOne: "Howdy"
# stringTwo: "Hewdy"

# Answer:
# True (since just would have to change the "e" in the second to an "o" or vice versa

# Multiple ways of solving

# 1. Check their lengths and see if they differ by more than 1. If so then, given our options, it's impossible to
# make them the same with only 1 edit. If they are the same length however, then check to see if the substring of
# the rest of the string after a difference is found is the same, if so then return True as they can be made
# the same with only 1 edit. Would need to iterate over both strings and make a substring to hold the characters to be
# checked.
# IE: "Howdy" and "Hewdy"
# When iterating over and at the 1st position of both strings, are at "o" and "e" respectively. Can do an edit at this
# point, either add or remove, to make them the same and then check if the following characters, "wdy" match up in both
# strings. If so that means we can return True, this only works for strings of the same length.
# IE2: "Howdy" and "Hwdy"
# For strings with different lengths, you'll have to make sure that after you find the character where they differ,
# if at all, and you either add or remove it. That the substring you check following the edit included or excludes the
# character that was either removed or added. So if "e" was removed from first string, would have to account for that
# when checking the following substring of "wdy" in both strings.

# Space Time Complexity:
# O(n + m) time (have to iterate through lengths of both strings)
# O(n + m) space (Have to account for substrings that are made from part of both strings when returning to check)


# 2. Same idea but now instead of checking for substrings, just check for more than 1 edit as you go while accounting
# for any edits already made in the strings.
# IE: "Howdy" and "Hwdy"
# Iterate through both strings, at the 1st position will find a difference of "o" in the first string and "w" in the
# second string. For now let's decide to remove the 


# Space Time Complexity
# O(n) time (since would only have to iterate to the end of one of the strings)
# O(1) space (since not using up any extra memory that would scale with the problem/input size)
