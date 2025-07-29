from typing import List
class Solution:
    """
    You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

    Return true if the Sudoku board is valid, otherwise return false
    """

    def isValidSudoku(self, board:List[List[str]]):
        
        for row in range(9):
            exist = set()
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in exist:
                    return False
                exist.add(num)
            #print(exist)
        for row in range(9):
            exist = set()
            for col in range(9):
                num = board[col][row]
                if num == '.':
                    continue
                if num in exist:
                    return False
        for box in range(9):
            exist=set()
            for r in range(3):
                for c in range(3):
                    row = (box//3)*3+r
                    col = (box%3)*3+c
                    num = board[col][row]
                    if num == '.':
                        continue
                    print(num)
                    if num in exist:
                        return False
                    exist.add(num)
        return True
'''
+-------+-------+-------+
| 1 2 . | . 3 . | . . . |
| 4 . . | 5 . . | . . . |
| . 9 8 | . . . | . . 3 |
+-------+-------+-------+
| 5 . . | . 6 . | . . 4 |
| . . . | 8 . 3 | . . 5 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . . . | . . . | 2 . . |
| . . . | 4 1 9 | . . 8 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+
'''

if __name__ == "__main__":
    board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    
    sol = Solution().isValidSudoku(board)
    print (sol)
    assert sol is True
    