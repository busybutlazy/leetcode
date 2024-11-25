from typing import List

class Solution:
    def __init__(self):
        self.step=1
        self.appeared=[]
        self.now_queue=[]
        self.next_queue=[]
        self.ans=[[1,2,3],[4,5,0]]
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def find_zero(board):
            zero_loc=[0,0]
            if 0 in board[1]:
                zero_loc[0]=1
            zero_loc[1]=board[zero_loc[0]].index(0)
            return zero_loc
        
        def move(board):
            zero_loc=find_zero(board)
            result=[]
            # swap up and down
            new_board=[board[0].copy(),board[1].copy()]
            new_board[0][zero_loc[1]],new_board[1][zero_loc[1]]=new_board[1][zero_loc[1]],new_board[0][zero_loc[1]]
            result.append(new_board)
            # swap left
            if zero_loc[1]!=0:
                new_board=[board[0].copy(),board[1].copy()]
                new_board[zero_loc[0]][zero_loc[1]-1],new_board[zero_loc[0]][zero_loc[1]]=new_board[zero_loc[0]][zero_loc[1]],new_board[zero_loc[0]][zero_loc[1]-1]
                result.append(new_board)
            # swap right
            if zero_loc[1]!=2:
                new_board=[board[0].copy(),board[1].copy()]
                new_board[zero_loc[0]][zero_loc[1]+1],new_board[zero_loc[0]][zero_loc[1]]=new_board[zero_loc[0]][zero_loc[1]],new_board[zero_loc[0]][zero_loc[1]+1]
                result.append(new_board)
            return result

        self.now_queue.append(board)
        
        now_board=[]
        self.appeared.append(board)
        
        if board==self.ans:
            return 0
        # Breadth-first-search
        while self.now_queue:
            now_board=self.now_queue.pop()
            for result in move(now_board):
                # Bingo! return the step
                if result == self.ans:
                    return self.step
                # Not the answer. It isn't a good answer if we seen it before.
                if result not in self.appeared:
                    self.appeared.append(result)
                    self.next_queue.append(result)
            if not self.now_queue:
                self.now_queue,self.next_queue=self.next_queue,[]
                self.step+=1
        return -1
        
if __name__ == '__main__':
    sol=Solution()
    board = [[4,1,2],[5,0,3]]
    print(sol.slidingPuzzle(board))