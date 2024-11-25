from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num=0
        max_length=1
        last_num=0
        curr_length=1
        for n in nums:
            if n!=last_num:
                # 結算
                max_length=max(max_length,curr_length)
                curr_length=1
                # 處理新數字
                if n > max_num:
                    max_num=n
                
            else:
                if n == max_num:
                    curr_length+=1
                else:
                    curr_length =1
            last_num=n

        return max_length
