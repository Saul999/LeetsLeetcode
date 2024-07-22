# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # nodes_set = set()
        # cur = head
        # if not cur or not cur.next:
        #     return False
        # while cur:
        #     if cur in nodes_set:
        #         return True
        #     if cur not in nodes_set:
        #         nodes_set.add(cur)
        #     cur = cur.next
        # return False

        ######################
        # Floyds T&H algo
        ######################
        
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
            if f == None:
                return False

        return False