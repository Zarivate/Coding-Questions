# Question:
# Given a string of length 12 or smaller with only digits. Write a function that returns all possible
# IP addresses that can be created by inserting three periods (.) within the string. All addresses 
# returned should be in string format in no particular order. If no valid IPs, return an empty list.

# Notes:
# Every digit created from insertion of the periods must be in range between 0-255 (inclusive).
# For this exercise, a valid IP can't have any leading 0s in any of it's sections. IE:
# 192.168.00.1 and 192.168.0.01 are both invalid
# Digits within input string will only ever be positive.
# Also this question is honestly really interesting due to it's optimal space and time complexity reasoning.

# Example:
example_string = "1921680"

# Answer:
output = ["1.9.216.80", "1.92.16.80", "1.92.168.0", 
          "19.2.16.80", "19.2.168.0", "19.21.6.80",
          "19.21.68.0", "19.216.8.0", "192.1.6.80",
          "192.1.68.0", "192.16.8.0"]

# **********************************************************************************************************************************
# O(1) time | O(1) space

# Time is O(1) because solution doesn't depend on size of input due to 2 reasons
# 1. At most input length will be 12
# 2. IPs are represented as 32 bit

# Using this you can calculate that at most, there are 2^32 possible IPs you will have to go through. You can calculate 
# this by using the knowledge that the max input length, 12, will be comprised of 4 8 bit sections. IE: Take the IP

# 172. 161. 254. 101
# These are 12 digits and can be represented in bits as
# 10101100. 10100001. 11111110. 01100101
# Each section is 8 bits (0-255), or 1 byte, added up together it comes out to 32 bits. Meaning you can surmise the max possibility
# of 2^32 IPS being possible.

# Which may sound like a lot, cause it honestly is, but in the case of Big O notation this would become a constant upperbound.
# Meaning the Big O time notation would go from O(2^32) to O(1) since constants get simplified. 

# Space is O(1) for similar reasons since, at most, the return list will be of size 2^32. In otherwords another uppper bound 
# that goes from O(2^32) to O(1).
# **********************************************************************************************************************************

# Explanation:
# The main idea on how to solve this, if you've noticed a pattern in the return output strings, is to break the digits into
# 4 separate parts. Each part is a possible valid IP and if the positions of the "." create 4 valid IPs, then add the resulting
# string into the return list. If not, then change the "." positions from right to left until find all possible combinations.

# Breakdown:
# 1921680

# Start by placing "." at the shortest possible distance from one another.
# 1. 9. 2. 1680
# Now check to see if each of these sections is valid
# 1 is valid
# 9 is valid
# 2 is valid
# 1680 is not valid

# Move "."s over by 1 starting from the rightmost one and repeat checking
# 1. 9. 21. 680
# 1 is valid
# 9 is valid
# 21 is valid
# 680 is not valid

# Repeat by moving right most "." over by 1
# 1. 9. 216. 80
# 1 is valid
# 9 is valid
# 216 is valid
# 80 is valid
# All valid so add to list

# Move onto second rightmost "." by moving it over by 1 and repeat checks
# 1. 92. 16. 80
# 1 is valid
# 92 is valid
# 16 is valid
# 80 is valid
# All valid so add to list

# Now because the second "." has moved over, that means the first "." has new possible combinations available so return
# to it and move the rightmost "." over by 1 again and check. This is also done because a valid IP between 0-255 can't have
# 4 digits without leading 0s. So wouldn't be possible to move the 
# 1. 92. 168. 0
# 1 is valid
# 92 is valid
# 168 is valid
# 0 is valid
# All valid so add to list

# Repeat this process until run out of possible combinations/"." shifts.


# Implementation:
def valid_ips(string):
 
    possibleIP = string
    ipsFound = []
 
    # Iterate through string, leave at least 2 open spaces for the other sections, is -2 because Python range() is exclusive
    for i in range(1, len(string) - 2):
        # Iterate again, starting from 1 position in front of the previous "." and up until the second to last position in string
        for j in range(i + 1, len(string) - 1):
            # Iterate again, now for the last sections, starting from 1 position in front of the last "." and up until the end of the string
            for k in range(j + 1, len(string)):
                # Create the IP sections by splicing together the ranges
                possibleIP = possibleIP[:k] + "." + possibleIP[k:]
                possibleIP = possibleIP[:j] + "." + possibleIP[j:]
                possibleIP = possibleIP[:i] + "." + possibleIP[i:]
                 
                # Check for the validity of combination
                if is_valid(possibleIP):
                    ipsFound.append(possibleIP)

                # Reset the possible IP string  
                possibleIP = string
                 
    return ipsFound

# Function to check validility of IP strings
def is_valid(ip):
 
    # Splitting by "."
    ip = ip.split(".")
     
    # Checking for edge cases
    for i in ip:
        # If the string section is longer than 3 digits or the integer is greater than 255, invalid
        if (len(i) > 3 or int(i) > 255):
            return False
        # Else if there are cases of multiple leading 0s, invalid.
        if len(i) > 1 and int(i) == 0:
            return False
        # Else check if ip is more than 1 digit, is not 0 but has a leading 0, if so invalid
        if (len(i) > 1 and int(i) != 0 and i[0] == '0'):
            return False
             
    return True
 
print(valid_ips(example_string))