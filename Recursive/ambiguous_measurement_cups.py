# Ambiguous Measurements

# Question:
# Given an array of measuring cups and two integers representing a target low and high value, return whether
# you can achieve the target ranges given the cup values provided.

# Notes:
# Can't pour contents of one cup into another
# Can be multiple ways to get answer, not just 1
# Low and high params will always follow the constraints, 0 <= low <= high and 0 <= L <= H
# Once you've measured some liquid, it'll be immediately transferred to a larger bowl that may eventually
# hold the target amount

# Example:
#                   L    H
sample_measuring_cups = [[200, 210],
                         [450, 465],
                         [800, 850]]

low = 2100
high = 2300


# Answer: True

# Note: Not only way to get to answer
# Use 4 cups of [450, 465] to first get 1800 and 1860
# Then use 2 cups of [200, 210] to get 2200 and 2280
# 2200 and 2280 are both in ranger of 2100 and 2300 so return True

# Optimal Space & Time Complexity:
# O(low * high * n) time
# O(low * high * n) space

# n = number of measuring cups
# At every call each cup is checked so "n" work is done at each call.
# The low * high represents the absolute max number of recursive calls we could have, also known as the upper bound

# Explanation:
# Main idea is to recognize that once we use a cup, we have a new low and high to aim for,
# IE: low = 2100 and high = 2300

# Using 1 cup [800, 850], we get
# 2100 - 800 = 1300 and 2300 - 850 = 1450 to get
# low = 1300 and high = 1450

# Using 1 more cup of [800, 850] to get
# 1300 - 800 = 500 and 1450 - 850 = 600 to get
# low = 500 and high = 600

# Using 1 more cup of [800, 850] we would get a negative answer, so instead try 1 cup of [450, 465] to get
# 500 - 450 = 50 and 600 - 465 = 135
# low = 50 and high = 135

# By now can see that any cup combo we try will get us outside the range, so means we can rule this combo out

# Using memoization, we can cache all of our solutions/ranges so if we ever come across the same range again, we
# can just look at the result stored in the HashTable and avoid repeated calls

# Possible solution 1:

def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return measure_in_range(measuringCups, low, high, memoization)


def measure_in_range(cups, low, high, memoization):
    memo_key = create_hashable_key(low, high)
    if memo_key in memoization:
        return memoization[memo_key]

    if low <= 0 and high <= 0:
        return False

    can_measure = False
    for cup in cups:
        cup_low, cup_high = cup
        if low <= cup_low and cup_high <= high:
            can_measure = True
            break

        new_low = max(0, low - cup_low)
        new_high = max(0, high - cup_high)
        can_measure = measure_in_range(cups, new_low, new_high, memoization)
        if can_measure:
            break

    memoization[memo_key] = can_measure
    return can_measure


def create_hashable_key(low, high):
    return str(low) + ":" + str(high)


# Possible solution 2: Foregoes hashing anything and instead using whatever (True/False) value is at the top
# of the call stack when returning answer

def ambiguous_measurements(measuring_cups, low, high):
    failed_combos = set()
    return measure_in_range(measuring_cups, low, high, 0, 0, failed_combos)


def measure_in_range(cups, low, high, current_low, current_high, failed_combos):
    # Set the current key to be the passed in low and high, in other words
    key = (current_low, current_high)
    print(key)

    # Check to see if the key is already in the set, if so return False
    if key in failed_combos:
        return False

    # If the current low passed in is greater than the high, than have exceeded range
    if current_low > high:
        # Add current key to failed combos set and return False
        failed_combos.add(key)
        return False

    if (current_high - current_low) > (high - low):
        # Add current key to failed combos set and return False
        failed_combos.add(key)
        return False

    # Have reached desired range, can return True
    if current_low >= low and high >= current_high:
        return True

    # Recursively try to reach range, add fluid from each cup
    for cup in cups:
        # Get the cup low and high values
        cup_low, cup_high = cup

        if measure_in_range(cups, low, high, current_low + cup_low, current_high + cup_high, failed_combos):
            return True
    # Add to set that can't find a range using these values
    failed_combos.add(key)
    return False


print(ambiguous_measurements(sample_measuring_cups, low, high))
