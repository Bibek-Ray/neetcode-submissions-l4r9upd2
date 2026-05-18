# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def nodeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_h = self.nodeHeight(root.left)
        if left_h == -1:
            return -1
        right_h = self.nodeHeight(root.right)
        if right_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1

        return max(self.nodeHeight(root.left), self.nodeHeight(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.nodeHeight(root) == -1:
            return False
        
        return True        