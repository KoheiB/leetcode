#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        # current1, current2 = l1, l2
        # number1, number2 = '', ''
        # while current1:
        #     number1 += str(current1.val)
        #     current1 = current1.next
        # while current2:
        #     number2 += str(current2.val)
        #     current2 = current2.next
        # reversed1: str = ''.join(reversed(number1))
        # reversed2: str = ''.join(reversed(number2))
        # added: int = int(reversed1) + int(reversed2)
        # reversed_added: str = ''.join(reversed(str(added)))
        # # 最初のノードを作成
        # head = ListNode(int(reversed_added[0]))
        # current = head

        # # 配列の残りの部分を順にノードに変換してリンクリストに追加
        # for value in reversed_added[1:]:
        #     current.next = ListNode(int(value))
        #     current = current.next

        # return head
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# @lc code=end
