from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        high=prices[0]
        spread=0
        for i in range(1,len(prices)):
            if prices[i-1]>prices[i]:
                spread+=high-low
                low=prices[i]
                high=prices[i]
                continue
            if prices[i]<low:
                low=prices[i]
            if prices[i]>high:
                high=prices[i]
        spread+=high-low
        return spread
            
                
        
        
        



prices=[1,2,3,4,5]
s=Solution()
print(s.maxProfit(prices))