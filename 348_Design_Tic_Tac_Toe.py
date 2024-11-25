from typing import List


class TicTacToe:
    def __init__(self, n):
        self.size=n
        self.row=[0]*n
        self.col=[0]*n
        self.left_top2right_down=0
        self.right_top2left_down=0

    def move(self,m:List[int])->int:
        to_add=-1 if m[2]!=1 else 1
        
        def check_win(m):            
            return self.row[m[0]]==self.size or self.col[m[1]]==self.size or self.left_top2right_down==self.size or self.right_top2left_down==self.size
        
        self.row[m[0]]+=to_add
        

        self.col[m[1]]+=to_add
        

        if m[0]==m[1]:
            self.left_top2right_down+=to_add
        
        if m[0]+m[1]==self.size-1:
            self.right_top2left_down+=to_add
        
        if check_win(m):
            return m[2]
        
        return 0


if __name__=="__main__":
    tictactoe=TicTacToe(3)
    inputs=[[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
    while inputs:
        print(tictactoe.move(inputs.pop(0)))