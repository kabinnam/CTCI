# Is Unique: Implement an algorithm to determine if
# a string has all unique characters. What if you
# cannot use additional data structures?
#
# Hints: #44, #117, #132

# Input: s, string
# Output: True (if all unique characters), False (otherwise)

def isUnique(s):
    return len(s) == len(set(s))

