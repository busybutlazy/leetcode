class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp=[[[0 for _ in range(n+1)]for _ in range(m+1)] for _ in range(k+1)]
        for l in range(1,k+1):
            for j in range(m+1):
                if j<l:
                    continue
                
                for i in range(n+1):
                    if i < l :
                        continue
                    # print("i=",i,"j=",j,"l=",l)
                    dp[l][j][i]=dp[l-1][j-1][i-1]+dp[l][j-1][i]+(dp[l][j][i-1]-dp[l][j-1][i-1])*j
                    if i == l :
                        dp[l][j][i]+=1
                
        return int(dp[-1][-1][-1]%(10e9+7))

    
n = 50
m = 100
k = 25

s=Solution()
print(s.numOfArrays(n, m, k))