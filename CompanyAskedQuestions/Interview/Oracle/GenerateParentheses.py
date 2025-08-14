# Problem Statement
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example:
    
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


# Approach (Backtracking)

# a)At each step, you can:
#     1)Add "(" if you still have left parentheses remaining.

#     2)Add ")" if it would not lead to more ) than (.

# b)Stop when the current string has 2 * n characters.



def generateParenthesis(n):
    res = []

    def backtrack(curr, open_count, close_count):
        # Base case: when string length is 2*n
        if len(curr) == 2 * n:
            res.append(curr)
            return
        
        # If we can add '(', do so
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)
        
        # If we can add ')', do so
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res

# Example usage
print(generateParenthesis(3))


# Dry Run for n=3

# 1)Start with ""

# 2)Add "(" until we reach 3 opens.

# 3)Add ")" when possible.

# 4)Backtrack and try alternative branches.
    
# Time Complexity
# 1)O(4ⁿ / √n) — The nth Catalan number complexity.

# space:
# 1)Space Complexity: O(n) for recursion stack.
