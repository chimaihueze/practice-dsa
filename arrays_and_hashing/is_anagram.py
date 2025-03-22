"""Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different."""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq_s = {}
    freq_t = {}

    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    return freq_s ==  freq_t
    
s = "racecar"
t = "carrace"
print(is_anagram(s, t))

s = "jar"
t = "jam"
print(is_anagram(s, t))
