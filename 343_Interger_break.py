class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        dp=[i for i in range(n+1)]
        for i in range(4,n+1):
            dp[i]=max(dp[i-2]*2,dp[i-3]*3)
        return dp
        
    
    
s=Solution()
n=10
print(s.integerBreak(n))