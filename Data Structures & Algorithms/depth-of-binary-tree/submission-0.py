# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        len_left = len_right = 0
        if not root:
            return 0
        else:
            len_left += 1 + self.maxDepth(root.left)
            len_right += 1 + self.maxDepth(root.right)
            return max(len_left, len_right)