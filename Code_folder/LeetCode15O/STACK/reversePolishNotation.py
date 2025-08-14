
# ✅ Problem Statement
# You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation (RPN).
# Evaluate the expression and return the result as an integer.

# Valid operators are "+", "-", "*", and "/".
# Each operand is a valid integer. Division should truncate toward zero.


# Example:
    
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22


# ✅ Approach: Stack
# 1)Use a stack to store operands.

# 2)Iterate over each token:

#     If it’s a number, push to stack.

#     If it’s an operator:

#         Pop two operands from the stack

#         Apply the operation

#         Push result back


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # Truncate toward zero
            else:
                stack.append(int(token))

        return stack[0]


# ✅ Example usage with input()
if __name__ == "__main__":
    # Input string: e.g., 2 1 + 3 *
    tokens = input("Enter the tokens separated by space (e.g., '2 1 + 3 *'): ").split()
    
    sol = Solution()
    result = sol.evalRPN(tokens)
    
    print("Result:", result)
    

# ✅ Key Notes:
# Integer division truncation toward zero is important.
# Python’s int(a / b) handles this correctly.
#     Example: int(-3 / 2) ➝ -1 (truncated toward 0, not -2)

# Use int(token) safely since all operands are valid integers.


# ✅ Time & Space Complexity
# | Operation | Complexity |
# | --------- | ---------- |
# | Time      | O(n)       |
# | Space     | O(n)       |
