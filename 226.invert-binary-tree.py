#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        def invert(node):
            if node == None:
                return None
            tmp = node.left
            node.left = node.right
            node.right = tmp
            invert(node.left)
            invert(node.right)
        invert(root)
        return (root)

# @lc code=end


