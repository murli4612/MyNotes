# Logic
# 1)Each node has:
# ------>Horizontal distance (HD) from root (root = 0, left child = HD - 1, right child = HD + 1).

# 2)Traverse using BFS.

# 3)For each HD, overwrite the value in a dictionary — the last node visited at that HD is the bottom view node.

# 4)Return nodes sorted by HD.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bottomView(root):
    if not root:
        return []

    # Queue will store tuple: (node, horizontal_distance)
    q = deque([(root, 0)])
    hd_map = {}  # horizontal distance -> last node value

    while q:
        node, hd = q.popleft()
        # Overwrite value for this horizontal distance
        hd_map[hd] = node.val

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    # Sort by horizontal distance and return values
    return [hd_map[hd] for hd in sorted(hd_map)]

# Example usage:
# Constructing the binary tree
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

print("Bottom View:", bottomView(root))
