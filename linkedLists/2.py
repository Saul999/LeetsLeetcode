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
        #creates new LL
        res = ListNode()
        #creates copy 
        cur = res
        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            #moves l1 and l2 to next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return res.next



