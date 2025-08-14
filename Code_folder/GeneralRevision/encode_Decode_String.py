def encodeDecodeString(strings):
    res = ""
    for s in strings:
        res += str(len(s)) + "#" + s
    return res


# def decodeString(string):
#     stack =[]
#     k = ""
#     for i in range(len(string)):
#         if string[i] == "#":
#             stack.append(string[i+1: i+1+ int(k)])
#             i = i + 1 + int(k)
#             k =""
#         else:
#             k = k + string[i]
#     return ''.join(stack)

# ❌ Problems:
# You're using a for loop, but also modifying i inside the loop (i = i + ...) – this doesn't work in Python for loops.

# ''.join(stack) returns a single combined string, but you probably meant to return a list of decoded strings.

# You should use a while loop to manually control i.
def decodeString(string):
    stack = []
    i = 0

    while i < len(string):
        k = ""
        # Read the number (length of next word)
        while i < len(string) and string[i] != '#':
            k += string[i]
            i += 1

        i += 1  # Skip the '#'

        length = int(k)
        word = string[i:i+length]
        stack.append(word)
        i += length

    return stack

# # Example usage
# encoded = "4#lint4#code4#love3#you"
# print(decodeString(encoded))  # Output: ['lint', 'code', 'love', 'you']

# Test
input_list = ["lint", "code", "love", "you"]
output = encodeDecodeString(input_list)
print(output)  # Output: 4#lint4#code4#love3#you
output_input= decodeString(output)
print(output_input)



# 📊 Time Complexity: O(N)
# Let N be the length of the input string.

# The loop processes each character exactly once, so total operations are proportional to N.

# 📦 Space Complexity: O(M)
# Let M be the total length of all decoded strings combined.

# The stack list stores the decoded words → takes O(M) space.

# Temporary variables like k, word, etc., are small → constant space.

# Time: O(N)

# Space: O(M) where M ≤ N
