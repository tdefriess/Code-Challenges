# https://leetcode.com/problems/linked-list-cycle-ii/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # make a dictionary of nodes with their value being their index position
        # traverse list
        # if next node has been encountered, return the index of the next node from dict
        
        encountered = {}
        current = head
        while current is not None and current.next is not None:
            if current.next in encountered:
                return current.next
            encountered[current] = pos
            current = current.next
        return None