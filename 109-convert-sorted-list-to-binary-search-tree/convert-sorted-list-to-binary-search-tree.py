# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        slow_prev.next = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root