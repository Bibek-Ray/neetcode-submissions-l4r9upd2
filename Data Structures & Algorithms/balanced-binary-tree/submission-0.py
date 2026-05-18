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
        return max(self.nodeHeight(root.left), self.nodeHeight(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        h_diff = abs(self.nodeHeight(root.left) - self.nodeHeight(root.right))
        return bool((h_diff <= 1) * self.isBalanced(root.left) * self.isBalanced(root.right)) 
        