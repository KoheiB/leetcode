#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def removeNthFromEnd(self, head, n: int):
#         dummy = ListNode(0)
#         dummy.next = head
#         fast, slow = dummy, dummy
#         for _ in range(n):
#             fast = fast.next
#         # i = 0
#         # while n > i:
#         #     fast = fast.next
#         #     i += 1
#         while fast:
#             fast, slow = fast.next, slow.next
#         slow.next= slow.next.next
#         return dummy.next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        # Move fast ahead by n+1 steps
        for _ in range(n + 1):
            fast = fast.next
        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next
        # Skip the nth node from the end
        slow.next = slow.next.next
        return dummy.next
        
# @lc code=end

