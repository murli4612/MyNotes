
# How it works:

# 1)We perform a standard BFS using a queue.

# 2)For each level, we append it to the front of a deque.

# 3)At the end, the deque naturally contains the reverse level order.
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseLevelOrder(root):
    if not root:
        return []

    queue = deque([root])
    result = deque()  # We use deque so we can appendleft efficiently

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.appendleft(current_level)  # Add each level to the front

    return list(result)  # Convert deque to list

# Example Usage
if __name__ == "__main__":
    # Constructing binary tree:
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(reverseLevelOrder(root))
    # Output: [[15, 7], [9, 20], [3]]


