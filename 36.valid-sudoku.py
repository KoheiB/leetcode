#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    # def isValidSudoku(self, board: [[str]]) -> bool:
        # def is_duplicated_array(array: [[str]]):
        #     s_map = {'1': 0, '2': 0, '3': 0, '4': 0,
        #                 '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        #     for s in array:
        #         if s != '.':
        #             s_map[s] += 1
        #             if s_map[s] > 1:
        #                 return True
        #         return False

        # def is_duplicated_array(array: [[str]]) -> bool:
        #     s_set = set()
        #     for s in array:
        #         if s != '.':
        #             if s in s_set:
        #                 return True
        #             s_set.add(s)
        #     return False

        # for row in board:
        #     if is_duplicated_array(row):
        #         return False

        # for i in range(9):
        #     col = [board[j][i] for j in range(9)]
        #     if is_duplicated_array(col):
        #         return False

        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         square = [board[i + x][j + y]
        #                   for x in range(3) for y in range(3)]
        #         if is_duplicated_array(square):
        #             return False
        # return True
    
    def isValidSudoku(self, board: [[str]]) -> bool:
        import collections
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# @lc code=end


Solution.isValidSudoku(None, [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])