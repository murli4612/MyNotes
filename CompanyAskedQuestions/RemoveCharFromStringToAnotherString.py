def RemoveCharFromStringComapreWithOther(StringA, RemoveString):
    remove_dict = {}
    result = []
    for char in RemoveString.lower():
        remove_dict[char] = remove_dict.get(char,0) + 1
        
    for char in StringA:
        if char in remove_dict:
            continue
        else:
            result.append(char)
    
    
    return ''.join(result)


print(RemoveCharFromStringComapreWithOther("careermonkc","ec"))


# function removeCharFromStringCompareWithOther(stringA, removeString) {
#     const removeDict = {};
#     const result = [];
    
#     for (const char of removeString.toLowerCase()) {
#         removeDict[char] = (removeDict[char] || 0) + 1;
#     }
    
#     for (const char of stringA) {
#         if (char in removeDict) {
#             continue;
#         } else {
#             result.push(char);
#         }
#     }
    
#     return result.join('');
# }

# console.log(removeCharFromStringCompareWithOther("careermonkc", "ec"));


def remove_chars_from_string(string_a, remove_string):
    remove_chars = set(remove_string.lower())
    return ''.join([char for char in string_a if char not in remove_chars])

print(remove_chars_from_string("careermonkc", "ec"))  # Output: "carrmonk"

# function removeCharsFromString(stringA, removeString) {
#     const removeChars = new Set(removeString.toLowerCase());
#     return [...stringA].filter(char => !removeChars.has(char)).join('');
# }

# console.log(removeCharsFromString("careermonkc", "ec"));  // Output: "carrmonk"


# Key Optimizations:
# Using Set instead of Dictionary:

# We don't need character counts, just membership check

# Sets provide O(1) lookup time (same as dictionaries but more memory efficient)

# List/Array Comprehension:

# Python: Using list comprehension is faster than appending in a loop

# JavaScript: Using filter() is cleaner than manual iteration

# Direct Conversion:

# Convert the remove string to lowercase once at the beginning

# Convert string to array directly (in JavaScript using spread operator)

# Simpler Logic:

# Removed unnecessary continue statement

# Combined the filtering into a single expression

# Performance Notes:
# The Set approach is faster for membership testing

# Both versions now have O(n + m) complexity where:

# n = length of input string

# m = length of remove string

# Memory usage is slightly better as we don't store counts we don't need

# Additional Optimization (if case sensitivity matters differently):