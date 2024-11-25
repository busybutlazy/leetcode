class Solution:
    def specialArray(self, nums) -> int:
        nums.sort(reverse=True)
        greater_num=1
        l=len(nums)
        if l<=nums[-1]:
            return l
        
        nums.append(0)        
        while l>greater_num:
            print("greater_num=",greater_num,"nums[greater_num-1]=",nums[greater_num-1],"nums[greater_num]=",nums[greater_num])
            if nums[greater_num]==nums[greater_num-1]:
                greater_num+=1
                continue
            if nums[greater_num]<greater_num and nums[greater_num-1]>=greater_num:
                return greater_num
            else:
                greater_num+=1
        return -1

if __name__ == '__main__':
    s=Solution()
    test_list=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    print(s.specialArray(test_list))