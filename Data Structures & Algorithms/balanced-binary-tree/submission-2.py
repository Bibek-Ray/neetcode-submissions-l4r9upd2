# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def nodeHeight(self, root: Optional[TreeNode]) -> Tuple:
        if not root:
            return (0, 1)
        left_node = self.nodeHeight(root.left)
        right_node = self.nodeHeight(root.right)
        return (max(left_node[0], right_node[0]) + 1, int(abs(left_node[0] - right_node[0]) <= 1))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_node = self.nodeHeight(root.left)
        right_node = self.nodeHeight(root.right)
        h_diff = abs(left_node[0] -right_node[0])
        return bool(int(h_diff <= 1) * left_node[1] * right_node[1]) 
        