from typing import List
from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        self.dp=defaultdict(int)
        
        def count_binary(nums):
            count=0
            while nums>0:
                nums=nums & (nums-1)
                count+=1
            return count
        
        def merge(arr1,arr2):
            sorted=[]
            while len(arr1) and len(arr2):
                if arr1[0] not in self.dp:
                    self.dp[arr1[0]]=count_binary(arr1[0])
                if arr2[0] not in self.dp:
                    self.dp[arr2[0]]=count_binary(arr2[0])
                
                
                if self.dp[arr1[0]]==self.dp[arr2[0]]:
                    if arr1[0]<arr2[0]:
                        sorted.append(arr1.pop(0))
                    else:
                        sorted.append(arr2.pop(0))
                elif self.dp[arr1[0]]<self.dp[arr2[0]]:
                    sorted.append(arr1.pop(0))
                else:
                    sorted.append(arr2.pop(0))
            if len(arr1)==0:
                sorted+=arr2
            else:
                sorted+=arr1
            return sorted
        l=len(arr)
        if l<2:
            return arr
        else:
            return merge(self.sortByBits(arr[:l//2]),self.sortByBits(arr[l//2:]))



arr = [0,1,2,3,4,5,6,7,8]
s=Solution()
print(s.sortByBits(arr))