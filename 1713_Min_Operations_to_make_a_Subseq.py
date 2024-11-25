from typing import List 

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pass
        # mapping arr to target
        target_map={}
        for i in range(len(target)):
            target_map.update({target[i]:i})
        arr_loction=[]
        for ele in arr:
            if ele in target_map:
                arr_loction.append(target_map[ele])
        
        if not arr_loction:
            return len(target)

        # lis question
        temp_lis=[arr_loction[0]]
        
        for i in range(1,len(arr_loction)):
            if arr_loction[i]>temp_lis[-1]:
                temp_lis.append(arr_loction[i])
            else:
                left=0
                right=len(temp_lis)-1
                while left<right:
                    mid=left+(right-left)//2
                    if temp_lis[mid]<arr_loction[i]:
                        left=mid+1
                    else:
                        right=mid
                temp_lis[left]=arr_loction[i]
        return len(target)-len(temp_lis)








if __name__=="__main__":
    solution=Solution()
    target=[6,4,8,1,3,2]
    arr=[4,7,6,2,3,8,6,1]
    print(solution.minOperations(target,arr))