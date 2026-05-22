# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, inorder, val, left, right) -> int:
        for i in range(left, right + 1):
            if inorder[i] == val:
                return i
        return -1

    def buildTreeRecur(self, preorder, inorder, preIndex, left, right):

        if left > right:
            return None
        
        rootVal = preorder[preIndex[0]]

        root = TreeNode(rootVal)
        preIndex[0] += 1
        
        index = self.search(inorder, rootVal, left, right)

        root.left = self.buildTreeRecur(preorder, inorder, preIndex, left, index - 1)
        root.right = self.buildTreeRecur(preorder, inorder, preIndex, index + 1, right)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = [0]
        
        return self.buildTreeRecur(preorder, inorder, preIdx, 0, len(inorder)-1)
        