#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        merged = []
            # ダミーノードを作成します
        dummy = ListNode(0)
        current = dummy
        
        # l1とl2の両方がNoneでない限り、ループします
        while l1 is not None and l2 is not None:
            # l1の値とl2の値を比較します
            if l1.val < l2.val:
                # l1の値が小さい場合、l1を新しいリンクリストに追加します
                current.next = l1
                l1 = l1.next
            else:
                # l2の値が小さい場合、l2を新しいリンクリストに追加します
                current.next = l2
                l2 = l2.next
            # 新しいリンクリストの現在のノードを進めます
            current = current.next
        
        # l1またはl2のどちらかがNoneになった場合、
        # もう一方のリンクリストの残りのノードを新しいリンクリストに追加します
        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        
        # ダミーノードの次のノードが、マージされたリンクリストのヘッドです
        return dummy.next

# @lc code=end

