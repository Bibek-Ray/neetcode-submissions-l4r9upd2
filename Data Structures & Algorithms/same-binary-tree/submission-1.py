# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False
        left_chk = self.isSameTree(p.left, q.left)
        if not left_chk:
            return False
        right_chk = self.isSameTree(p.right, q.right)
        if not right_chk:
            return False
        return True