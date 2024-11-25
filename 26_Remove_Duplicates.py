from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set=set()
        record=0
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                record+=1
                nums_set.add(nums[i])
            nums[i],nums[record-1]=None,nums[i]
        print(nums)
        return record

nums = [1,1,2]
s=Solution()
print(s.removeDuplicates(nums))