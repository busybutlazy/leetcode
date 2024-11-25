class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 0
        if n==1:return 3
        if n==2:return 8
        MOD=int(1000000007)
        dp=[[0 for _ in range(5)] for _ in range(n+1)]
        to_minus=0
        for i in range(n+1):
            if i ==0 :continue
            if i ==1:
                dp[i][0]=dp[i][1]=dp[i][2]=dp[i][3]=dp[i][4]=1
            elif i==2:
                dp[i][0]=3
                dp[i][1]=3
                dp[i][2]=2
                dp[i][3]=2
                dp[i][4]=2
            else:
                sum_of=sum(dp[i-1][:3])%MOD
                dp[i][0]=sum_of
                dp[i][1]=(dp[i-1][0]+dp[i-2][0]+dp[i-1][2]+dp[i-2][2])%MOD
                dp[i][3]=(dp[i-1][3]+dp[i-1][4])%MOD
                dp[i][4]=(dp[i-1][3]+dp[i-2][3])%MOD
                dp[i][2]=(dp[i-1][3]+dp[i-1][4])%MOD
        return sum(dp[-1][:3])%MOD

if __name__ == '__main__':
    s=Solution()
    n=2
    print(s.checkRecord(n))       