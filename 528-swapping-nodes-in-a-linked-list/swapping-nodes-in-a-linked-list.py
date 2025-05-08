# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        n  =  head
        for _ in range(k-1):
            n  =  n.next
        
        a  =  n
        b  =  head
        
        while n.next:
            b  =  b.next
            n  =  n.next
        
        a.val, b.val  =  b.val, a.val
        
        return head