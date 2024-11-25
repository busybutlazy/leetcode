from typing import List


class Solution:
    def __init__(self) -> None:
        self.dp=[-1]*2001
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # for t in range(target+1):
        #     prev=0
        #     for i in range(len(nums)):
        #         if nums[i] == t:
        #             prev+=1
        #         elif nums[i] < t:
        #             prev+=self.dp[t-nums[i]]
        #     self.dp[t]=prev
        # return self.dp[target]
        pass
        self.com_helper(nums,target)
        return self.dp[target]
    
    def com_helper(self,nums,target):
        result=0
        for i in range(len(nums)):
            if nums[i] > target:
                self.dp[target]=0
            elif nums[i] == target:
                result+=1
            elif nums[i] < target:
                if self.dp[target-nums[i]]==-1:
                    self.com_helper(nums,target-nums[i])
                result+=self.dp[target-nums[i]]
        self.dp[target]=result
                
s=Solution()
nums = [10,7,9]
target = 92
print(s.combinationSum4(nums=nums,target=target))