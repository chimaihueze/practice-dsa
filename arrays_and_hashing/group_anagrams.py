"""
URL -> https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 

but the order of the characters can be different.
"""


def group_anagrams(strs):

    string_dict = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key in string_dict: string_dict[key].append(word)
        else: string_dict[key] = [word]

    output = [value for key, value in string_dict.items()]
    
    return output


strs = ["act","pots","tops","cat","stop","hat"]

print(group_anagrams(strs))

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

strs = ["x"]

print(group_anagrams(strs))

# Output: [["x"]]

strs = [""]

print(group_anagrams(strs))

# Output: [[""]]

