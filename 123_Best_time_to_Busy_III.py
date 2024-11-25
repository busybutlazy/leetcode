from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_trade=self.find_best_spread(prices)
        if len(prices)<4:
            return one_trade
        first_trade=self.find_best_spread(prices[:2])
        second_trade=self.find_best_spread(prices[2:])
        two_trade=first_trade+second_trade
        
        for i in range(2,len(prices)-1):
            if prices[i-1]>prices[i-2]:
                first_trade=self.find_best_spread(prices[0:i])
            if prices[i]>prices[i-1]:
                second_trade=self.find_best_spread(prices[i:])
            print("i=",i,"/",len(prices)," first_trade=",first_trade,"second_trade=",second_trade)
            if two_trade<first_trade+second_trade:
                two_trade=first_trade+second_trade
        return max(one_trade,two_trade)
    
    def find_best_spread(self,prices):
        low=prices[0]
        spread=0
        for p in prices:
            
            if p<low:
                low=p
                continue
            if spread<p-low:
                spread=p-low
        return spread        
    
    
    

s=Solution()
# print(s.maxProfit(prices))
# print(s.find_best_spread(prices[5:]))