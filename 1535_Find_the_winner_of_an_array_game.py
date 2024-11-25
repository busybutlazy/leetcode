from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >len(arr):return max(arr)
        arr2=arr[:k]
        arr2.sort()
        arr=arr+arr2[:k-1]
        if arr[0]==max(arr[:k+1]):return arr[0]
        slow_pointer=1
        fast_pointer=k
        tmp_max=max(arr[:k])
        
        while fast_pointer<len(arr):
            if tmp_max<arr[fast_pointer]:
                tmp_max=arr[fast_pointer]
            if arr[slow_pointer]==tmp_max: return tmp_max
            slow_pointer+=1
            fast_pointer+=1
        
        
    

arr = [2,1,3,5,4,6,7]
k = 2
s=Solution()
print(s.getWinner(arr,k))