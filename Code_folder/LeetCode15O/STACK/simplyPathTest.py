# import unittest
# import sys
# import os

# Add the project root to sys.path
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
# from simplyPath import  Solution

# class TestSimplifyPath(unittest.TestCase):
#     def setUp(self):
#         self.solution = Solution()

#     def test_simple_path(self):
#         self.assertEqual(self.solution.simplifyPath("/home/"), "/home")

#     def test_trailing_slash(self):
#         self.assertEqual(self.solution.simplifyPath("/home//foo/"), "/home/foo")

#     def test_dot_and_dotdot(self):
#         self.assertEqual(self.solution.simplifyPath("/a/./b/../../c/"), "/c")

#     def test_only_dotdot(self):
#         self.assertEqual(self.solution.simplifyPath("/../"), "/")

#     def test_nested_folders(self):
#         self.assertEqual(self.solution.simplifyPath("/a//b////c/d//././/.."), "/a/b/c")

#     def test_empty_root(self):
#         self.assertEqual(self.solution.simplifyPath("/"), "/")

#     def test_complex_path(self):
#         self.assertEqual(self.solution.simplifyPath("/a/../../b/../c//.//"), "/c")

# if __name__ == '__main__':
#     unittest.main()

# File: test_simplify_path.py

# import unittest
# from simplyPath import  simplifyPath

# class TestSimplifyPath(unittest.TestCase):
#     def test_examples(self):
#         self.assertEqual(simplifyPath("/home/"), "/home")
#         self.assertEqual(simplifyPath("/../"), "/")
#         self.assertEqual(simplifyPath("/home//foo/"), "/home/foo")
#         self.assertEqual(simplifyPath("/a/./b/../../c/"), "/c")
#         self.assertEqual(simplifyPath("/a/../../b/../c//.//"), "/c")
#         self.assertEqual(simplifyPath("/a//b////c/d//././/.."), "/a/b/c")
#         self.assertEqual(simplifyPath("/."), "/")
#         self.assertEqual(simplifyPath("/..."), "/...")

# if __name__ == "__main__":
#     unittest.main()


# # Test input
# input_path = "/a/./b/../../c/"
# print(simplifyPath(input_path))  # Output: /c


import pytest
from simplyPath import simplifyPath

@pytest.mark.parametrize("input_path, expected", [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/a/../../b/../c//.//", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c"),
    ("/.", "/"),
    ("/...", "/..."),
])
def test_simplify_path(input_path, expected):
    assert simplifyPath(input_path) == expected

