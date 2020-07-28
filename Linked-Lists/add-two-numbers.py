# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        carry = 0
        while l1 or l2 or carry:
            newVal = 0
            if l1:
                newVal += l1.val
            if l2:
                newVal += l2.val
            newVal += carry
            carry, val = divmod((newVal), 10)
            current.val = val
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                current.next = ListNode(0)
                current = current.next
        
        return head