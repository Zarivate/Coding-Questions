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
# second string. For now let's decide to remove the "o". Keep track that used up first and only edit and keep iterating
# through the strings. However, iterate only in the bigger string once. Will make it so the pointer for string 1 is
# at "l" and pointer for string two also at "l". After this, keep iterating like normal until find any more differences.
# If you do, then return false, else return True.
# IE2: "Howdy" and "Hewdy"
# The "replace" case/same string length case is even easier, instead of having to only iterate through the bigger string
# like before, now just keep iterating as normal after finding a difference and keep track if any other difference shows
# up. Since if one does, then return False else return True.


# Space Time Complexity
# O(n) time (since would only have to iterate to the end of one of the strings)
# O(1) space (since not using up any extra memory that would scale with the problem/input size)

# Edit these values to test out function
first_string = "Howdy"
second_string = "Hwdy"


# First solution implementation
def oneEditFirstSolution(stringOne, stringTwo):
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)

    # If the difference in their lengths is greater than 1, than that means
    # more than 1 edit will be required. Thus return false.
    if abs(lengthOne - lengthTwo) > 1:
        return False

    # Go to the end of the shorter string
    for i in range(min(lengthOne, lengthTwo)):
        # Check whether characters match
        if stringOne[i] != stringTwo[i]:
            # If the first string is longer than the second
            if lengthOne > lengthTwo:
                # Return whether the first string's current position + 1, up till the end substring matches
                # with the substring of the second string's current position to the end
                return stringOne[i + 1:] == stringTwo[i:]
            # Else if string two is longer, do the same but now for the second string
            elif lengthTwo > lengthOne:
                return stringOne[i:] == stringTwo[i + 1:]
            else:
                return stringOne[i + 1:] == stringTwo[i + 1:]

    return True


# Second solution implementation
def oneEdit(stringOne, stringTwo):
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)

    # If the difference in their lengths is greater than 1, than that means
    # more than 1 edit will be required. Thus return false.
    if abs(lengthOne - lengthTwo) > 1:
        return False

    editDone = False
    pointerOne, pointerTwo = 0, 0

    while pointerOne < lengthOne and pointerTwo < lengthTwo:
        # If a character in the same position of both strings doesn't match
        if stringOne[pointerOne] != stringTwo[pointerTwo]:
            # Check to see if an edit has already been made
            # If so return false, else set it to True and continue
            if editDone:
                return False
            editDone = True

            # If the first string is longer, than increment it's pointer by 1
            if lengthOne > lengthTwo:
                pointerOne += 1
            # Else if the second string is longer, increment it's pointer by 1
            elif lengthTwo > lengthOne:
                pointerTwo += 1
            # If the strings are the same length, just increment both their pointers by 1
            else:
                pointerOne += 1
                pointerTwo += 1
        # Else if the characters were the same, just increment the pointers and keep going
        else:
            pointerOne += 1
            pointerTwo += 1

    return True


print(oneEditFirstSolution(first_string, second_string))
print(oneEdit(first_string, second_string))

