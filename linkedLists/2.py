# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        cur = res
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else: 
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val) 
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next
            

