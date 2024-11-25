class Solution:
    def __init__(self):
        self.step_map=[[-1 for _ in range(101)]for _ in range(101)]
        
    def uniquePaths(self, m: int, n: int) -> int:
        # if n==1 or m==1:
        #     self.step_map[m][n]=1
        #     self.step_map[n][m]=1
        #     return 1
        # if self.step_map[m-1][n]==-1:
        #     self.step_map[m-1][n]=self.uniquePaths(m-1,n)
        # if self.step_map[m][n-1]==-1:
        #     self.step_map[m][n-1]=self.uniquePaths(m,n-1)
        # self.step_map[m][n]=self.step_map[m-1][n]+self.step_map[m][n-1]
        # return self.step_map[m][n]
        if m==1 or n==1:
            return 1
        m=m-1
        prev_row=[1 for _ in range(n)]
        now_row=[1 for _ in range(n)]
        
        for _ in range(m):
            for j in range(1,n):
                now_row[j]=now_row[j-1]+prev_row[j]
            prev_row=now_row
            # print(prev_row)
        
        return now_row[-1]
        
        
            
solution=Solution()
print(solution.uniquePaths(13,23))
