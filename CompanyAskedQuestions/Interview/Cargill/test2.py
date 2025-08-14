# Given a string s, find the length of the longest substring without repeating characters.

# Example
# Input: s = "abcabcbb"
# Output: 3

# Explanation: The longest substrings without repeating characters are "abc", "bca", and "cab", all with length 3.
def longest_sub_string(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for i in range(len(s)):
        if s[i] in char_index and char_index[s[i]]>= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        max_length = max(max_length, i - start + 1)
    return max_length


# s = "abcabcbb"
# s = "pw wke w"
print(longest_sub_string(s))