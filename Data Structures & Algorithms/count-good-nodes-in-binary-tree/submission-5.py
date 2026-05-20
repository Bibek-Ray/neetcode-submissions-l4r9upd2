# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        ct = 1

        q.append((root, root.val))
        while len(q) != 0:
            levelsize = len(q)
            for i in range(levelsize):
                node_val =  q.popleft()
                node = node_val[0]
                max_so_far = node_val[1]
                if node.left:
                    q.append((node.left, max(max_so_far, node.left.val)))
                    ct += 1 if node.left.val >= max_so_far else 0
                if node.right:
                    q.append((node.right, max(max_so_far, node.right.val)))
                    ct += 1 if node.right.val >= max_so_far else 0

        return ct
