from typing import List
from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        two_sum_map=defaultdict(list)
        num_counter=defaultdict(int)
        flag=False
        for i in range(len(nums)):
            num_counter[nums[i]]+=1
            if num_counter[nums[i]]>4:
                flag=True

        if flag:
            print("flag is True")
            nums=[]
            for num in num_counter:
                nums=nums+[num]*min(num_counter[num],4)
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if [nums[i],nums[j]] in two_sum_map[nums[i]+nums[j]]:
                    continue
                two_sum_map[nums[i]+nums[j]].append([nums[i],nums[j]])

        print("two_sum_map=",two_sum_map)
        print("num_counter=",num_counter)

        result=[]
        
        def check_valid(li:List[int])->bool:
            for num in li:
                if li.count(num)>num_counter[num]:
                    return False
            return True
            
                


        for two_sum in two_sum_map:
            if target-two_sum in two_sum_map:
                # combine and check
                for list1 in two_sum_map[two_sum]:
                    for list2 in two_sum_map[target-two_sum]:
                        combine_list=list1+list2
                        combine_list.sort()
                        if check_valid(combine_list) and combine_list not in result:
                            result.append(combine_list)

        return list(result)


    

if __name__=="__main__":
    solution=Solution()
    nums=[1,2,0,0,-1,-2]*200
    target=0
    print(solution.fourSum(nums,target))