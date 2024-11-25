from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        nums1,nums2=[0]+nums1,[0]+nums2        
        check_positive=False
        tmp=float("-inf")
        dp=[[0 for _ in range(len(nums1))]for _ in range(len(nums2))]
        # value and index
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if i ==0 or j==0:
                    continue
                dp[i][j]=max(dp[i][j-1],dp[i-1][j-1]+nums2[i]*nums1[j],dp[i-1][j])
                if check_positive==False:
                    tmp=max(nums2[i]*nums1[j],tmp)
                    if nums2[i]*nums1[j]>0:
                        check_positive=True
        if check_positive : 
            return dp[-1][-1] 
        else : 
            return tmp
                    
                
                
    
    
    
    
nums1 = [-1,-1]
nums2 = [1,1]


s=Solution()
print(s.maxDotProduct(nums1,nums2))