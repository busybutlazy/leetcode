from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_num=len(nums1)+len(nums2)
        median=[]
        median.append((total_num)//2)
        median.append((total_num-1)//2)
        print("median=",median)
        merge_list=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2) and len(merge_list)<median[0]+1:
            if nums1[i]<=nums2[j]:
                merge_list.append(nums1[i])
                i+=1
            else:
                merge_list.append(nums2[j])
                j+=1
        if i==len(nums1):
            merge_list.extend(nums2[j:])
        if j==len(nums2):
            merge_list.extend(nums1[i:])
        return (merge_list[median[0]]+merge_list[median[1]])/2

        
                    
    
nums1 = [1]
nums2 = [2,4,7,8,13]
f=Solution().findMedianSortedArrays
print(f(nums1, nums2))