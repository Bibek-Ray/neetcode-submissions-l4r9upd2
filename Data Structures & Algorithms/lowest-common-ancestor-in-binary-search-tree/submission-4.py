# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not (root.left and root.right):
            return root
        left_nd, right_nd = p if p.val < q.val else q, q if p.val < q.val else p 
        if left_nd.val <= root.val and root.val <= right_nd.val:
            return root
        if left_nd.val <= root.val and right_nd.val <= root.val:
            return self.lowestCommonAncestor(root.left, left_nd, right_nd)
        if not (left_nd.val <= root.val and right_nd.val <= root.val):
            return self.lowestCommonAncestor(root.right, left_nd, right_nd)