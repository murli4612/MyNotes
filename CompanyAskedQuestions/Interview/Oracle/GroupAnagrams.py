from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))   # e.g., "eat" -> "aet"
        groups[key].append(s)
    return list(groups.values())

# Example
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]


# 1)Time: O(N * K log K) — K = avg length of string

# 2)Space: O(N * K)


# 2) Using letter counts as the key (faster for large K, assumes lowercase a–z)
from collections import defaultdict

def groupAnagrams_count(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0]*26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

print(groupAnagrams_count(["eat","tea","tan","ate","nat","bat"]))

# Time: O(N * K)

# Space: O(N)
