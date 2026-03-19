# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
