#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # ハッシュマップの初期化
        hashmap = {}

        # 1回目の反復: 各ノードのディープコピーを作成
        current = head
        while current:
            hashmap[current] = Node(current.val)
            current = current.next

        # 2回目の反復: `next`と`random`ポインタを設定
        current = head
        while current:
            if current.next:
                hashmap[current].next = hashmap[current.next]
            if current.random:
                hashmap[current].random = hashmap[current.random]
            current = current.next

        # 新しいリストのヘッドを返す
        return hashmap[head]


# @lc code=end
