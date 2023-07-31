#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
# class Solution:
#     def groupAnagrams(self, strs: [str]) -> [[str]]:
#         anagram_dict = {} # anagram : [str]
#         for str in strs:
#             anagram = ''.join(sorted(str))
#             if anagram in anagram_dict:
#                 anagram_dict[anagram].append(str)
#             else:
#                 anagram_dict[anagram] = [str]
#         print(list(map(lambda x: x, anagram_dict.values())))
#         return list(map(lambda x: x, anagram_dict.values()))
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        print(ans)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
            print(ans)
        return ans.values()


# tupleもdictのキーにもてる

# 以下ChatGPTより

# 不変な型（Immutable Type）:
# 文字列（str）
# 数値（int, float, complex）
# タプル（tuple）
# ブール値（bool）
# frozenset（凍結されたセット）

# 注意点:
# 辞書のキーは重複しない必要があります。同じキーが複数回現れた場合、最後の値が保持されます。
# キーには変更可能な型（リストやセットなど）は使用できません。変更可能な型をキーにすると、辞書のハッシュテーブルの仕組みによって予測不可能な振る舞いが生じる可能性があります。
# キーにはNoneを使用することもできます。

# @lc code=end

