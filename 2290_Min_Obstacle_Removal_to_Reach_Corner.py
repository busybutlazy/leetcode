from typing import List
import collections

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        step_record=[[float("inf")]*len(grid[0]) for _ in range(len(grid))]
        step_record[0][0]=0

        def get_posible_next_loc(loc):
            x,y=loc
            candidates=[]
            # go down
            if x< len(grid)-1:
                candidates.append((x+1,y))
            # go up
            if x>0:
                candidates.append((x-1,y))
            # go right
            if y< len(grid[0])-1:
                candidates.append((x,y+1))
            # go left
            if y >0:
                candidates.append((x,y-1))
            return candidates
        
        q=collections.deque([(0,0)])
        
        while q:    
            x,y=q.popleft()
            for next_x,next_y in get_posible_next_loc((x,y)):
                # Returning to (x, y) doesn't require rechecking.
                if (x,y)==(next_x,next_y):continue
                
                # If it is a better solution, we have to recheck the neighboring points.
                # Otherwise, we can do nothing.
                if step_record[next_x][next_y]>step_record[x][y]+1:
                    
                    # We can search the neighbors of the point that is blocked later.
                    if grid[next_x][next_y]:
                        q.append((next_x,next_y))
                        step_record[next_x][next_y]=step_record[x][y]+1
                    else:
                        q.appendleft((next_x,next_y))
                        step_record[next_x][next_y]=step_record[x][y]

        return step_record[-1][-1]

if __name__=="__main__":
    solution=Solution()
    grid = [[0,1,1,1,1,0],[1,1,0,0,1,0],[0,0,1,1,0,0],[0,1,1,1,0,1],[1,0,0,1,1,1],[1,1,0,1,0,0],[1,1,0,0,1,0]]
    print(solution.minimumObstacles(grid))