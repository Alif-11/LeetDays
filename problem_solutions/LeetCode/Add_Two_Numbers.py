# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: 
Optional[ListNode]) -> Optional[ListNode]:
        """
        Date: 8/11/2023
        Time: 16:03
        * Purpose: Add two numbers, given two you as two linked lists in reverse, 
        * and return the reverse linked list version of their sum
        Runtime: 58 ms, beats 96.54% What!!??
        Memory: 16.56 mb, beats 30.18%, not bad
        """
        a = l1
        b = l2
        l_node = ListNode(0, None)
        head = l_node # we'll return this, don't touch 
        remainder = 0
        """ until both a and b BOTH have no more nodes left, keep adding.
            when you a and b BOTH have no more nodes left, then check 
remainder.
            * if remainder is nonzero, make a new node to l_node with a 
value
            * of 1 and return 'head'.
            else, just return 'head' """
        while(True):
            remainder = 0
            # * if the below conditional is met, then we had to carry a 1 
            # * from the previous addition. In that case, just return
            if (a == None and b == None):
                return head
            c = a.val + b.val + l_node.val
            if c >= 10:
                c -= 10
                remainder = 1
            l_node.val = c
            # making sure we're not at the end of both numbers
            if (a.next != None or b.next != None):
                if (a.next == None):
                    a.next = ListNode(0, None)
                if (b.next == None):
                    b.next = ListNode(0, None)
                if not remainder:
                    l_node.next = ListNode(0, None)
            # how we carry the one
            if remainder:
                l_node.next = ListNode(1, None)
            a = a.next
            b = b.next
            l_node = l_node.next
            if (a == None and b == None and not remainder):
                break
        return head
