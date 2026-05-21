# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBST(self, root, low_bound: int, up_bound: int) -> bool:
        if not root:
            return True

        if root.val > low_bound and root.val < up_bound:
            return self.checkBST(root.left, low_bound, root.val) and self.checkBST(root.right, root.val, up_bound)
        
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.checkBST(root, -1001, 1001)