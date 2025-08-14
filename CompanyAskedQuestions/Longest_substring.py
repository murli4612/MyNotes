class Solution:
    def lengthOfLongestSubstring(self, s: str):
        map = {}
        max_length = start =0
        left_side = 0
        start_idx = 0  # To remember start of longest substring
        
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                if i - start + 1 > max_length:
                    max_length = max(max_length, i - start + 1)
                    longest_substring = s[start:start + max_length]
            map[s[i]] = i

        # for right_side in range(len(s)):
        #     if s[right_side] in char_map and char_map[s[right_side]] >= left_side:
        #         left_side = char_map[s[right_side]] + 1

        #     char_map[s[right_side]] = right_side

        #     # Update max_length and start index of substring
        #     if right_side - left_side + 1 > max_length:
        #         max_length = right_side - left_side + 1
        #         start_idx = left_side

        longest_substring = s[start_idx:start_idx + max_length]
        return max_length, longest_substring

# Example usage:
sol = Solution()
s = "abcabcbb"
length, substring = sol.lengthOfLongestSubstring(s)
print(f"Length: {length}")
print(f"Longest Substring: '{substring}'")
