from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums=nums
        self.dp=[-1 for i in range(len(nums))]
        for i in range(len(nums)):
            self.find_increase(i)
        return max(self.dp)
        
    def find_increase(self,idx):
        if self.dp[idx]!=-1:
            return self.dp[idx]
        
        max_val=1
        for i in range(idx+1,len(self.nums)):
            if self.nums[i]>self.nums[idx]:
                max_val=max(max_val,self.find_increase(i)+1)
        self.dp[idx]=max_val
        return self.dp[idx]



if __name__ == '__main__':
    solution=Solution()
    nums=[0,1,0,3,2,3]
    print(solution.lengthOfLIS(nums))