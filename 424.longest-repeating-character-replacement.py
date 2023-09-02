#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        # int型のデフォルト値を持つdefaultdictを作成
        char_dict = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            char_dict[s[r]] += 1
            max_val = max(char_dict.values())
            if (r - l + 1) - max_val > k:
                char_dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    # この問題を解くための一般的なアプローチは、スライディングウィンドウを使用することです。ウィンドウのサイズを増やしながら、ウィンドウ内の最も頻繁に現れる文字の数とウィンドウのサイズの差が k 以下であるかを確認します。もし差が k より大きい場合、ウィンドウの左側を1つずらします。この方法で、操作を k 回以下で行って最も長い部分文字列を見つけることができます。

# @lc code=end
input = {
    'self': None,
    's': 'ABAA',
    'k': 0
}
Solution.characterReplacement(**input)