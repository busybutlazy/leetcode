class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result=[]
        tmp_sum=None
        for i in range(len(nums)):
            if i <k or i>=len(nums)-k:
                result.append(-1)
            else:
                if tmp_sum==None:
                    tmp_sum=sum(nums[i-k:i+k+1])
                else:
                    tmp_sum=tmp_sum-nums[i-k-1]+nums[i+k]
                result.append(tmp_sum//(2*k+1))
                

        return result        
        
        
ga=Solution().getAverages
nums=[7,4,3,9,1,8,5,2,6]
k=3
print(ga(nums, k))