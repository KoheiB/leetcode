#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # prev = None
        # current = head
        # while current:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        # return prev
        prev = None          # 初期化：prevは最初はNoneに設定されます。
        cur = head           # 初期化：cur（現在のノード）はリストの先頭に設定されます。
        while cur:           # curがNoneになるまで、つまりリストの最後まで繰り返します。
            next_node = cur.next # next_nodeはcurの次のノードに設定されます。
            cur.next = prev     # curの次のノードをprevに設定し、リンクの方向を逆にします。
            prev = cur          # prevを次の反復のためにcurに設定します。
            cur = next_node     # curを次の反復のためにnext_nodeに設定します。
        head = prev           # リストの先頭をprevに設定します。これでリストが逆転します。
        return head            # 逆転したリストの先頭を返します。

# @lc code=end


