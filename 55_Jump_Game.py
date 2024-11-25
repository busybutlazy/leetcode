from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:return True
        nums.reverse()
        # print(nums)
        dfs=[0]        
        while dfs:
            print("dfs=",dfs)    
            now_idx=dfs.pop()
            print("now_idx=",now_idx)

            for i in range(len(nums)-1,now_idx,-1):
                print("nums[i]=",nums[i],"i=",i)
                
                if nums[i]>=i-now_idx:
                    if i==len(nums)-1:
                        return True
                    dfs.append(i)
                    break
                
        return False
                    
            
        






if __name__ == "__main__":
    solution=Solution()
    nums=[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(solution.canJump(nums))