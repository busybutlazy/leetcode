from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_set=set()
            for j in range(9):
                if board[i][j]==".":continue
                elif board[i][j] in check_set:
                    return False
                else: check_set.add(board[i][j])
        for i in range(9):
            check_set=set()
            for j in range(9):
                if board[j][i]==".":continue
                elif board[j][i] in check_set:
                    return False
                else: check_set.add(board[j][i])
        check=set(["1","2","3","4","5","6","7","8","9"])
        for i in range(0,9,3):
            for j in range(0,9,3):
                if len(set(board[i][j:j+3])&set(board[i+1][j:j+3])&check)>0 or len(set(board[i+1][j:j+3])&set(board[i+2][j:j+3])&check)>0 or len(set(board[i][j:j+3])&set(board[i+2][j:j+3])&check)>0:
                    return False
        return True
                    
    
s=Solution()
ivs=s.isValidSudoku
board = [[".","2",".",".",".",".",".",".","."],
         [".",".",".",".",".",".","5",".","1"],
         [".",".",".",".",".",".","8","1","3"],
         ["4",".","9",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","2",".",".",".",".",".","."],
         ["7",".","6",".",".",".",".",".","."],
         ["9",".",".",".",".","4",".",".","."],
         [".",".",".",".",".",".",".",".","."]]
print(ivs(board))
# for i in range(0,9,3):
#     for j in range(0,9,3):
#         print(i,j)            