#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # def is_duplicated_array(array: [[str]]):
        #     s_map = {'1': 0, '2': 0, '3': 0, '4': 0,
        #                 '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        #     for s in array:
        #         if s != '.':
        #             s_map[s] += 1
        #             if s_map[s] > 1:
        #                 return True
        #         return False

        def is_duplicated_array(array: [[str]]) -> bool:
            s_set = set()
            for s in array:
                if s != '.':
                    if s in s_set:
                        return True
                    s_set.add(s)
            return False

        for row in board:
            if is_duplicated_array(row):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if is_duplicated_array(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[i + x][j + y]
                          for x in range(3) for y in range(3)]
                if is_duplicated_array(square):
                    return False
        return True
# @lc code=end
