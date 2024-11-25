from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        self.dp=[[0 for _ in range(amount+1)] for _ in range(len(coins)+1) ]
        coins=[0]+coins
        for i in range(len(coins)):
            for j in range(amount+1):
                if i == 0:
                    continue
                if coins[i] == j:
                    self.dp[i][j]+=1
                if coins[i] <j:
                    self.dp[i][j]+=self.dp[i][j-coins[i]]
                self.dp[i][j]+=(self.dp[i-1][j])
        return self.dp[-1][-1]
    
s=Solution()
change=s.change
amount = 12
coins = [2,3,5]
print(change(amount,coins))