from typing import List
from collections import deque


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        nums.sort(reverse=True)
        # print(nums)
        my_stack=deque()
        now_max=[nums[0],float("inf")]
        step_to_move=0
        previous_num=nums[0]
        for i in range(1,len(nums)):
            
            # print("now_max=",now_max,"nums[i]=",nums[i],"previous_num=",previous_num)
            if previous_num-nums[i]>1:
                tmp=[nums[i],previous_num-nums[i]-1]
                my_stack.append(now_max)
                now_max=tmp
            elif previous_num==nums[i]:
                now_max[0]+=1
                # print("step_to_move add ",now_max[0]-nums[i])
                step_to_move+=now_max[0]-nums[i]
                now_max[1]-=1
                if now_max[1]==0:
                    now_max=my_stack.pop()
                
            previous_num=nums[i]
        return step_to_move
    
if __name__=="__main__":
    nums=[13,11,4,6,4,0,0,5,3,7,2,3,10,11,4]
    print(Solution().minIncrementForUnique(nums))