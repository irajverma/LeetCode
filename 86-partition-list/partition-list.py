# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        
        dummyNode1=ListNode(0)
        dummyNode2=ListNode(0)

        lesser=dummyNode1
        greater=dummyNode2

        curr=head

        while curr!=None:

            if curr.val<x:

                lesser.next=curr
                lesser=lesser.next

            elif curr.val>=x:

                greater.next=curr
                greater=greater.next
            curr=curr.next

        greater.next=None
        lesser.next=dummyNode2.next

        return dummyNode1.next

        