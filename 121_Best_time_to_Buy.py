from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        spread=0
        for p in prices:
            if p<low:
                low=p
                continue
            if spread<p-low:
                spread=p-low
        return spread
    
prices = [7,1,5,3,6,4]
s=Solution()
print(s.maxProfit(prices))