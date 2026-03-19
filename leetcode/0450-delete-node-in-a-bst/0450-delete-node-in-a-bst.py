# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.left:
                root = root.right
                return root
            elif not root.right:
                root = root.left
                return root
            temp = root.left
            root = root.right
            if not root.left:
                root.left = temp
                return root
            node = root.left
            while node and node.left:
                node = node.left
            node.left = temp
            return root
        node = root
        parent = root
        while node:
            if node.val > key:
                parent = node
                node = node.left
                
            elif node.val < key:
                parent = node
                node = node.right
            
            else :
                temp = node.left

                if node == parent.left:
                    if not node.right:
                        parent.left = temp
                        break
                    parent.left = node.right
                    node = node.right
                    while node and node.left:
                        node = node.left
                    node.left = temp
                    break
                elif node == parent.right:
                    parent.right = node.right
                    if not node.right:
                        parent.right = temp
                        break
                    node = node.right
                    while node and node.left:
                        node = node.left
                    node.left = temp
                    break
        
        return root