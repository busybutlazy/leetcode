from typing import List

class Solution:
    def __init__(self):
        self.dp=[[0 for _ in range(201)]for _ in range(201)]
    
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_num=len(dungeon)-1
        col_num=len(dungeon[0])-1
        for i in range(row_num,-1,-1):
            for j in range(col_num,-1,-1):
                right_num=self.dp[i][j+1]
                if j==col_num:
                    right_num=self.dp[i+1][j]
                down_num=self.dp[i+1][j]
                if i==row_num:
                    down_num=self.dp[i][j+1]
                self.dp[i][j]=max(down_num+dungeon[i][j],right_num+dungeon[i][j])
                self.dp[i][j]=min(self.dp[i][j],0)
        return 1-(self.dp[0][0])
            
        
        
        
        
        # for r in range(row_num,0,-1):
        #     print("outer")
        #     self.dp[r][col_num]=self.dp[r+1][col_num]+dungeon[r-1][col_num-1]    
        #     for c in range(col_num-1,0,-1):
        #         if r==row_num:
        #             self.dp[r][c]=self.dp[r][c+1]+dungeon[r-1][c-1]
        #             self.dp[r][c]=min(self.dp[r][c],0)
        #         else:
        #             self.dp[r][c]=max(self.dp[r][c+1]+dungeon[r-1][c-1],self.dp[r+1][c]+dungeon[r-1][c-1])
        #             self.dp[r][c]=min(self.dp[r][c],0)
        #     print("r=",r,"c=",c,"map=",self.dp[r][c])
        # self.dp[1][1]=min(self.dp[1][1],0)
        # return 1-self.dp[1][1]


solution=Solution()
dungeon=[[-3,5]]
print(solution.calculateMinimumHP(dungeon))
