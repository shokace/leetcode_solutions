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
        node = ListNode()
        carry = 0
        current = node

        while l1 or l2 or carry:

            if l1:
                digit1 = l1.val
            else:
                digit1 = 0

            if l2:
                digit2 = l2.val
            else:
                digit2 = 0

            val = digit1 + digit2 + carry
            carry = val / 10
            val = val % 10
            current.next = ListNode(val)

            current = current.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return node.next


