# 📝 Problem Statement:
    
# Given a string path, which is an absolute path (starting with a slash /) to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system:

#     1)A period . refers to the current directory.

#     2)A double period .. refers to the directory up a level.

#     3)Multiple slashes '//' are treated as a single slash '/'.

# Return the simplified canonical path.


# 🔒 Constraints:
# 1 <= path.length <= 3000

# path consists of English letters, digits, period '.', slash '/', and underscores '_'.

# path is a valid absolute Unix path.


# ✨ Example 1:
    
# Input:  path = "/home/"
# Output: "/home"


# 2)
# Input:  path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, since the root is the highest level.

# 3)
# Input:  path = "/home//foo/"
# Output: "/home/foo"

# 4)
# Input:  path = "/a/./b/../../c/"
# Output: "/c"

# 🔍 Step-by-step Breakdown:
    
# 1)Split the path by slashes /
#  a--> This gives us segments like ["", "a", ".", "b", "..", "..", "c", ""]
#  b--> Empty strings or . mean "stay in current directory", so we skip them.

# 2)Initialize a stack
#   -->This will keep track of the directory structure as we process the path.

# 3)Process each part:
#     -->If it's .. → pop the last valid directory (go up one level)
#     -->If it's . or "" → ignore
#     -->Otherwise → push it to the stack (move into that directory)
# 4)Rebuild the final path
#     -->Join the stack with '/' and prefix it with a single /.


# ✅ Example Dry Run
# Input:
#     path = "/a/./b/../../c/"

# Step-by-step:
#     1)Split path: ['', 'a', '.', 'b', '..', '..', 'c', '']
#     2)Processing:
#         ->'' → skip

#         ->'a' → stack = ['a']

#         ->'.' → skip

#         ->'b' → stack = ['a', 'b']

#         ->'..' → pop 'b' → stack = ['a']

#         ->'..' → pop 'a' → stack = []

#         ->'c' → stack = ['c']

#         ->'' → skip
#    3)Join: '/' + 'c' → "/c"


# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#         for part in path.split('/'):
#             if part == '..':
#                 if stack:
#                     stack.pop()  # Go back to parent directory
#             elif part and part != '.':
#                 stack.append(part)  # Valid directory name, move into it
#         return '/' + '/'.join(stack)


# # Input and Output Handling
# if __name__ == "__main__":
#     path = input("Enter the path: ")  # Example: "/a/./b/../../c/"
#     sol = Solution()
#     simplified = sol.simplifyPath(path)
#     print("Simplified path:", simplified)


# def simplifyPath(path):
#     stack = []
#     for part in path.split('/'):
#         if part == '..':
#             if stack:
#                 stack.pop()  # Go back to parent directory
#         elif part and part != '.':
#             stack.append(part)  # Valid directory name, move into it
#     return '/' + '/'.join(stack)

# # Test input
# input_path = "/a/./b/../../c/"
# print(simplifyPath(input_path))  # Output: /c

def simplifyPath(path):
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.' and part != '_':
            stack.append(part)
    return '/' + '/'.join(stack)

# Input containing underscore as a folder name
input_path = "/a/_/b/.."
print("Simplified Path:", simplifyPath(input_path))

# 🧠 Time and Space Complexity

# | Metric | Value |
# | ------ | ----- |
# | Time   | O(n)  |
# | Space  | O(n)  |

