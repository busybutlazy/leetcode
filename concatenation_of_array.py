class Solution(object):
    def getConcatenation(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2=nums.copy()
        return nums+nums2
        
        
s=Solution().getConcatenation

nums = [1,2,1]
print(s(nums))