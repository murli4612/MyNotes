
def first_non_repeated_char(s):
    char_count = {}

    # Count occurrences
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Find first with count 1
    for ch in s:
        if char_count[ch] == 1:
            return ch

    return None

# Example:
print(first_non_repeated_char("swiss"))  # Output: w
print(first_non_repeated_char("aabbcc")) # Output: None

# function firstNonRepeatedChar(str) {
#   const charCount = {};

#   // Count occurrences
#   for (const char of str) {
#     charCount[char] = (charCount[char] || 0) + 1;
#   }

#   // Find first with count 1
#   for (const char of str) {
#     if (charCount[char] === 1) {
#       return char;
#     }
#   }

#   return null; // or '' if none found
# }

# // Example:
# console.log(firstNonRepeatedChar("swiss"));  // Output: 'w'
# console.log(firstNonRepeatedChar("aabbcc")); // Output: null

# 1. Case-insensitive first non-repeated character
# JavaScript:

# function firstNonRepeatedCharCaseInsensitive(str) {
#   const charCount = {};
#   const lowerStr = str.toLowerCase();

#   for (const char of lowerStr) {
#     charCount[char] = (charCount[char] || 0) + 1;
#   }

#   for (let i = 0; i < lowerStr.length; i++) {
#     if (charCount[lowerStr[i]] === 1) {
#       return str[i];  // return original case char
#     }
#   }

#   return null;
# }

# console.log(firstNonRepeatedCharCaseInsensitive("Swiss")); // Output: 'w'

# Python:
def first_non_repeated_char_case_insensitive(s):
    s_lower = s.lower()
    char_count = {}

    for ch in s_lower:
        char_count[ch] = char_count.get(ch, 0) + 1

    for i, ch in enumerate(s_lower):
        if char_count[ch] == 1:
            return s[i]  # return original case char

    return None

print(first_non_repeated_char_case_insensitive("Swiss"))  # Output: w

# 2. Return index of first non-repeated character
# JavaScript:

# function indexFirstNonRepeatedChar(str) {
#   const charCount = {};

#   for (const char of str) {
#     charCount[char] = (charCount[char] || 0) + 1;
#   }

#   for (let i = 0; i < str.length; i++) {
#     if (charCount[str[i]] === 1) {
#       return i;
#     }
#   }

#   return -1; // not found
# }

# console.log(indexFirstNonRepeatedChar("swiss"));  // Output: 1 (index of 'w')
# console.log(indexFirstNonRepeatedChar("aabbcc")); // Output: -1
# 
# Python:
def index_first_non_repeated_char(s):
    char_count = {}

    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if char_count[ch] == 1:
            return i

    return -1

print(index_first_non_repeated_char("swiss"))  # Output: 1
print(index_first_non_repeated_char("aabbcc")) # Output: -1


# 3. More efficient approach
# If you want to do it in one pass, you can store indexes and counts:

# JavaScript example (single pass):
# function firstNonRepeatedCharSinglePass(str) {
#   const charMap = new Map();

#   for (let i = 0; i < str.length; i++) {
#     if (!charMap.has(str[i])) {
#       charMap.set(str[i], { count: 1, index: i });
#     } else {
#       charMap.get(str[i]).count++;
#     }
#   }

#   let firstIndex = str.length;
#   let firstChar = null;

#   for (const [char, data] of charMap.entries()) {
#     if (data.count === 1 && data.index < firstIndex) {
#       firstIndex = data.index;
#       firstChar = char;
#     }
#   }

#   return firstChar;
# }

# console.log(firstNonRepeatedCharSinglePass("swiss"));  // Output: w
