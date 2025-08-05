from typing import List
class Solution:
    """
    You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

    Return true if the Sudoku board is valid, otherwise return false
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                val = int(board[row][col]) -1
                
                if (1<<val)&rows[row]:
                    for r in rows:
                        print(bin(r))
                    return False
                if (1<<val)&cols[col]:
                    for c in cols:
                        print(bin(c))
                    return False
                if (1<<val) & boxes[(row//3) * 3 + (col//3)]:
                    for b in boxes:
                        print(bin(b))
                    return False
                rows[row] |= (1<<val)
                cols[col] |= (1<<val)                
                boxes[(row//3) * 3 + (col//3)] |= (1<<val)
        return True
'''
+-------+-------+-------+
| . . 4 | . . . | 6 3 . |
| . . . | . . . | . . . |
| 5 . . | . . . | . 9 . |
+-------+-------+-------+
| . . . | 5 6 . | . . . |
| 4 . 3 | . . . | . . 1 |
| . . . | 7 . . | . . . |
+-------+-------+-------+
| . . . | 5 . . | . . . |
| . . . | . . . | . . . |
| . . . | . . . | . . . |
+-------+-------+-------+
'''

if __name__ == "__main__":
    board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    
    sol = Solution().isValidSudoku(board)
    print (sol)
    