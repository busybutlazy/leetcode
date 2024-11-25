class Solution(object):
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=set()
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                tmp=nums[i]+nums[j]+nums[k]
                if (tmp==0):
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif (tmp<0):
                    j+=1
                else:
                    k-=1
        return list(result)
        

s=Solution().threeSum
nums = [-1,0,1,2,-1,-4]
print(s(nums))

