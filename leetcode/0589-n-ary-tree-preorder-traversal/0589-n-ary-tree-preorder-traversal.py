"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def backtrack(node):
            res.append(node.val)
            #print(res)

            for c_node in node.children:
                backtrack(c_node)
        backtrack(root)
        #print(res)
        return res
            
