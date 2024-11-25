class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dic={}
        for i in range(len(nums)):
            if nums[i] in num_dic:
                num_dic[nums[i]].append(i)
            else:
                num_dic.update({nums[i]:[i]})
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -nums[i]-nums[j] in num_dic :
                    for k in num_dic[-nums[i]-nums[j]]:
                        if k>j:
                            ans.append([nums[i],nums[j],nums[k]])
        
        return ans
        # ans=[]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        

s=Solution().threeSum
nums = [-1,0,1,2,-1,-4]
print(s(nums))
nums = [0,1,1]
print(s(nums))
nums = [0,0,0]
print(s(nums))
