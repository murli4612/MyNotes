def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example
numbers = [3, 2, 1, 2, 4, 3, 1, 5]
print(remove_duplicates(numbers))  # Output: [3, 2, 1, 4, 5]


# function removeDuplicates(arr) {
#     const result = [];
#     for (const item of arr) {
#         if (!result.includes(item)) {  // Checks if item is already in 'result'
#             result.push(item);  // Adds item only if not present
#         }
#     }
#     return result;
# }

# // Example
# const numbers = [3, 2, 1, 2, 4, 3, 1, 5];
# console.log(removeDuplicates(numbers));  // Output: [3, 2, 1, 4, 5]

# Key Differences & Notes
# Time Complexity:

# Python: O(n²) (because item not in result scans the list for each element).

# JavaScript: O(n²) (because includes() scans the array for each element).

# Optimization (Better for Large Lists):

# Python: Use dict.fromkeys() (faster, O(n)):

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# JavaScript: Use Set (faster, O(n)):
    
# function removeDuplicates(arr) {
#     return [...new Set(arr)];
# }

# Here's the Python implementation to remove duplicates from a list while preserving order, with time and space complexity analysis:

# Python Solution (Preserving Order)

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
numbers = [3, 2, 1, 2, 4, 3, 1, 5]
print(remove_duplicates(numbers))  # Output: [3, 2, 1, 4, 5]

# Time and Space Complexity Analysis

# Time Complexity: O(n)

# We iterate through the list once (O(n))

# Set membership checks are O(1) on average

# List appends are O(1) amortized

# Space Complexity: O(n)

# We store all unique elements in a set (O(n) in worst case)

# We build a new result list (O(n) in worst case)

# Alternative Optimized Versions
# 1. Using dict.fromkeys() (Python 3.7+):
    
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# Time: O(n) (single pass)

# Space: O(n) (dictionary storage)

# 2. Using OrderedDict (Python < 3.7):

from collections import OrderedDict
def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

# 3. Using a list comprehension (less efficient):

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Performance Comparison
# Method	Time Complexity	Space Complexity	Preserves Order
# Set + Loop	O(n)	O(n)	Yes
# dict.fromkeys()	O(n)	O(n)	Yes (Python 3.7+)
# OrderedDict	O(n)	O(n)	Yes
# Naive (item in list)	O(n²)	O(n)	Yes

# The recommended approach is either:

# set() + loop (most readable)

# dict.fromkeys() (most concise in Python 3.7+)

# Both have optimal O(n) time and space complexity while preserving order.