# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        def preord (node):
            if node:
                preorder.append(node.val)
                preord(node.left)
                preord(node.right)
            
        preord(root)
        return preorder