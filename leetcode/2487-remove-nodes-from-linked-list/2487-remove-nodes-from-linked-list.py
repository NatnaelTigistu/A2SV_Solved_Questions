# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
  
        while curr is not None:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        head = ListNode(stack[0])
        curr = head
        for val in stack[1:]:
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next
        return head