def decodeString(s):
    stack = []
    # for i in range(len(s)):
    #     char = s[i]
    for char in s:
    # for i in range(len(s)):
    #     char = s[i]
        if char != ']':
            stack.append(char)
        else:
            # Get the string inside brackets
            substr = ''
            while stack and stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()  # remove the '['

            # Get the repeat count (can be more than one digit)
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            # Repeat and push back
            stack.append(substr * int(k))

    return ''.join(stack)

# Test
input_str = "3[a]2[bc]"
print(decodeString(input_str))  # Output: aaabcbc
