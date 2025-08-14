# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Codec:

#     # Encodes a tree to a single string using preorder traversal.
#     def serialize(self, root):
#         def dfs(node):
#             if not node:
#                 vals.append('#')
#                 return
#             vals.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)

#         vals = []
#         dfs(root)
#         return ','.join(vals)

#     # Decodes your encoded data to tree using preorder.
#     def deserialize(self, data):
#         def dfs():
#             val = next(vals)
#             if val == '#':
#                 return None
#             node = TreeNode(int(val))
#             node.left = dfs()
#             node.right = dfs()
#             return node

#         vals = iter(data.split(','))
#         return dfs()
    

# # ----------------------------
# # 🔄 Example Usage (Optional):
# # ----------------------------

# def print_inorder(root):
#     if not root:
#         return
#     print_inorder(root.left)
#     print(root.val, end=' ')
#     print_inorder(root.right)

# # Create a sample tree:
# #         1
# #        / \
# #       2   3
# #          / \
# #         4   5

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.right.left = TreeNode(4)
# tree.right.right = TreeNode(5)

# codec = Codec()

# # Serialize the tree
# serialized = codec.serialize(tree)
# print("Serialized Tree:", serialized)

# # Deserialize it back
# deserialized_tree = codec.deserialize(serialized)

# print("Inorder Traversal of Deserialized Tree:", end=' ')
# print_inorder(deserialized_tree)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    # Serialize tree using preorder traversal with '#' as null marker
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return ','.join(vals)

    # Deserialize using index tracking instead of iterator
    def deserialize(self, data):
        vals = data.split(',')
        index = [0]  # using a list so it acts like a reference

        def dfs():
            if index[0] >= len(vals):
                return None

            val = vals[index[0]]
            index[0] += 1

            if val == '#':
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# ----------------------------
# ✅ Example Usage:
# ----------------------------

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=' ')
    print_inorder(root.right)

# Build example tree:
#         1
#        / \
#       2   3
#          / \
#         4   5

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

codec = Codec()

# Serialize
serialized = codec.serialize(tree)
print("Serialized Tree:", serialized)

# Deserialize
deserialized_tree = codec.deserialize(serialized)
print("Inorder Traversal of Deserialized Tree:", end=' ')
print_inorder(deserialized_tree)
