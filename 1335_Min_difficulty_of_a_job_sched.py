from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        l=len(jobDifficulty)
        
        if d>l:return -1
        
        dp=[[float("inf") for _ in range(l)]for _ in range(d)]
        for i in range(d):
            for j in range(l):
                if i == 0 :
                    if j==0:
                        dp[i][j]=jobDifficulty[j]
                    else:
                        dp[i][j]=max(dp[i][j-1],jobDifficulty[j])
                else:
                    if j<i:continue
                    
                    
                    tmp_small_result,tmp_big_result=float("inf"),float("inf")
                    flag=True
                    for k in range(j-1,-1,-1):
                        tmp_big_result=min(dp[i-1][k],tmp_big_result)
                        if jobDifficulty[j]<jobDifficulty[k]:
                            tmp_small_result=dp[i][k]
                            flag=False
                            break
                            
                    
                    
                    dp[i][j]=min(dp[i-1][j-1]+jobDifficulty[j],tmp_small_result,tmp_big_result+jobDifficulty[j])
                    
                    
        return dp
    
sol=Solution()
jobDifficulty = [186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360]
d = 4
print(sol.minDifficulty(jobDifficulty,d))