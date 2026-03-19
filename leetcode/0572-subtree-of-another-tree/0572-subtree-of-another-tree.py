# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            stackp = [p]
            stackq = [q]
            i = 0
            while stackp and stackq:
                pnode = stackp.pop()
                qnode = stackq.pop()

                if (not pnode and qnode) or (not qnode and pnode):
                    print('f')
                    print(i)
                    return False
                if pnode and qnode:        
                    if pnode.val != qnode.val:
                        print('s')
                        return False
                    stackp.append(pnode.left)
                    stackq.append(qnode.left)
                    stackp.append(pnode.right) 
                    stackq.append(qnode.right) 
                i += 1
            if stackp != stackq:
                return False
            return True

        stack = [root]
        potential = []
        substack = [subRoot]
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    if isSameTree(node,subRoot):
                        return True
                stack.append(node.left)
                stack.append(node.right)
        return False


