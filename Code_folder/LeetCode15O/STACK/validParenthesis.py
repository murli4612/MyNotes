# Problem Statement

# Given a string s containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

# A string is valid if:

# 1)Open brackets must be closed by the same type of brackets.

# 2)Open brackets must be closed in the correct order.

# 3)Every close bracket has a corresponding open bracket of the same type.

# Example
# Input:
# s = "()"
# Output:
# true

# Input:
# s = "()[]{}"
# Output:
# true

# Input:
# s = "(]"
# Output:
# false

# Approach
# We use a stack:
    
# 1)Traverse each character in the string.
# 2)If it's an opening bracket (, [, {, push it onto the stack.
# 3)If it's a closing bracket ), ], }, check if the top of the stack is its matching opening bracket.

# -------------a)If yes, pop it.

# -------------b)If no or stack is empty, return false.

# 4)In the end, if the stack is empty, return true, otherwise false.

def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


# Time and Space Complexity
# 1)Time Complexity: O(n) (We scan the string once.)

# 2)Space Complexity: O(n) (In the worst case, all characters are opening brackets.)