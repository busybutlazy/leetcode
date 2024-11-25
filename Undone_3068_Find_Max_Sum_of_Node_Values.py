from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        print()
        
        # counter=0
        # min_change=0
        # flag=False
        # for edge in edges:
        #     if nums[edge[1]]==nums[edge[1]]^k:
        #         flag=True
        #     elif nums[edge[1]]<nums[edge[1]]^k:
        #         min_change=min(min_change,nums[edge[1]]^k-nums[edge[1]])
        #         nums[edge[1]]=nums[edge[1]]^k
        #         counter+=1
        
        # if flag:
        #     nums[edges[0][0]]=max(nums[edges[0][0]],nums[edges[0][0]]^k)
        #     return sum(nums)
        
        
        # if counter%2==0:
        #     if nums[edges[0][0]]>=nums[edges[0][0]]^k:
        #         return sum(nums)
        #     else:
        #         if nums[edges[0][0]]^k-nums[edges[0][0]]>min_change:
        #             return sum(nums)+(nums[edges[0][0]]^k-nums[edges[0][0]])-min_change
        #         else:
        #             return sum(nums)
        # else:
        #     if nums[edges[0][0]]<=nums[edges[0][0]]^k:
        #         nums[edges[0][0]]=nums[edges[0][0]]^k
        #         return sum(nums)
        #     else:
        #         if nums[edges[0][0]]-nums[edges[0][0]]^k>min_change:
        #             return sum(nums)+(nums[edges[0][0]]-nums[edges[0][0]]^k)-min_change
        #         else:
        #             return sum(nums)
                
    

if __name__=="__main__":
    nums=[24,78,1,97,44]
    k=6
    edges=[[0,2],[1,2],[4,2],[3,4]]#260
    print(Solution().maximumValueSum(nums,k,edges))