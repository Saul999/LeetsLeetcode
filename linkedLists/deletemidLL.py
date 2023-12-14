# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head and not head.next:
            return None

        if head and head.next and not head.next.next:
            head.next = None
            return head

        doubleJump = head.next.next
        singleJump = head
        lastnode = singleJump
        singleJump = singleJump.next
        while True:

            if doubleJump.next and not doubleJump.next.next:
                doublejump = doubleJump.next
                lastnode = singleJump
                singleJump = singleJump.next
                lastnode.next = None
                lastnode.next = singleJump.next
                singleJump.next = None
                return head

            if not doubleJump or not doubleJump.next or not doubleJump.next.next:
                lastnode.next = None
                lastnode.next = singleJump.next
                singleJump.next = None
                return head

            doubleJump = doubleJump.next.next
            lastnode = singleJump
            singleJump = singleJump.next

        return head
