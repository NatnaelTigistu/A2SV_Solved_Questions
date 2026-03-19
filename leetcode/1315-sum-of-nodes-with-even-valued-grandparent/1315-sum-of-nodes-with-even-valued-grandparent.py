# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def sum(node):
            gc1 = node.left.left.val if node.left and node.left.left else 0
            gc2 = node.left.right.val if node.left and node.left.right else 0
            gc3 = node.right.left.val if node.right and node.right.left else 0
            gc4 = node.right.right.val if node.right and node.right.right else 0
            return gc1+gc2+gc3+gc4
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val % 2 == 0:
                    total += sum(node)
                stack.append(node.left)
                stack.append(node.right)
        
        return total
