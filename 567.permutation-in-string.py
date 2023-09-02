#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            if c not in s1_map:
                s1_map[c] = 0
            s1_map[c] += 1
        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                return False
            target = s2[i:i+len(s1)]
            target_map = {}
            for c in target:
                if c not in target_map:
                    target_map[c] = 0
                target_map[c] += 1
            if s1_map == target_map:
                return True


# @lc code=end
input = {
    'self': None,
    's1': "ab",
    's2': "eidbaooo"
}
Solution.checkInclusion(**input)
