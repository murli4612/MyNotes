
from collections import defaultdict
def groupAnagrams(words):
    # group_anagrams = defaultdict(list)
    group_anagrams ={}
    for word in words:
        word_key = tuple(sorted(word))
        if word_key in group_anagrams:
            group_anagrams[word_key].append(word)
        else:
            group_anagrams[word_key] = [word]
            
        # group_anagrams[word_key].append(word)
    # print(group_anagrams)
    return list(group_anagrams.values())
        
        
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs1))