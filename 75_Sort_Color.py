from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        low,mid,hight=0,0,len(nums)-1

        while mid <= hight:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
                
            elif nums[mid]==1:
                mid+=1
                
            elif nums[mid]==2:
                nums[hight],nums[mid]=nums[mid],nums[hight]
                hight-=1
        
        
        
        # count={0:0,1:0,2:0}
        # for num in nums:
        #     count[num]+=1
        # index=0
        # for i in range(3):
        #     while count[i]>0:
        #         nums[index]=i
        #         count[i]-=1
        #         index+=1


if __name__=="__main__":
    nums=[2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)