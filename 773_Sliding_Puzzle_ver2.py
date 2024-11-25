from typing import List

class Solution:
    def __init__(self):
        self.step=1
        self.appeared=set()
        self.now_queue=[]
        self.next_queue=[]
        self.ans="123450"
        self.movable={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def move(now_board:str):
            loc=now_board.index("0")
            result=[]
            for go_to in self.movable[loc]:
                new_board=""
                for i in range(len(now_board)):
                    if i == loc:
                        new_board+=now_board[go_to]
                    elif i == go_to:
                        new_board+=now_board[loc]
                    else:
                        new_board+=now_board[i]
                result.append(new_board)
            return result
            
        now_board=""
        for row in board:
            for num in row:
                now_board+=str(num)
                
        self.now_queue.append(now_board)
        self.appeared.add(now_board)
        
        if now_board==self.ans:
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
                    self.appeared.add(result)
                    self.next_queue.append(result)

            if not self.now_queue:
                self.now_queue,self.next_queue=self.next_queue,[]
                self.step+=1
        return -1
        
if __name__ == '__main__':
    sol=Solution()
    board = [[4,1,2],[5,0,3]]
    print(sol.slidingPuzzle(board))