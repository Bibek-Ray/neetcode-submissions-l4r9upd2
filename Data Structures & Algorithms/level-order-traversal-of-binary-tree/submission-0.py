# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque() 
        p = deque()
        ls = []

        q.append(root)
        p.append(root.val)
        while len(q) != 0:
            levelsize = len(q)
            ls.append(list(p))
            for i in range(levelsize):
                node = q.popleft()
                p.popleft()
                if node.left:
                    q.append(node.left)
                    p.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    p.append(node.right.val)
        
        return ls