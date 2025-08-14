def find_duplicates(s):
    freq = {}
    duplicates = set()

    for char in s:
        freq[char] = freq.get(char, 0) + 1
        # if freq[char] > 1:
        #     duplicates.add(char)
    for key,freq1 in freq.items():
        if freq1 > 1:
            print(key) 
    # return duplicates

# Example usage
s = "programming"
find_duplicates(s) # Output: {'g', 'r', 'm'}


