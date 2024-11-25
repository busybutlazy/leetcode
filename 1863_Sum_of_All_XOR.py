# class Solution(object):
#     def subsetXORSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_list=self.recursive(nums)
#         result=0
#         for num in num_list:
#             result+=self.xor_cal(num)
#         return result

#     def recursive(self,nums):
#         if nums==[]:
#             return [[]]
#         else:
#             to_add=self.recursive(nums[1:])
#             return [[nums[0]]+sub for sub in to_add]+to_add
        
#     def xor_cal(self,nums):
#         result=0
#         for n in nums:
#             result=result^n
#         return result


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list=self.recursive(nums)
       
        return sum(num_list)

    def recursive(self,nums):
        if nums==[]:
            return [0]
        else:
            to_add=self.recursive(nums[1:])
            result=[nums[0]^sub for sub in to_add]
            result+=to_add
            return result


if __name__=="__main__":
    s=Solution()
    to_test=[3,4,5,6,7,8]
    print(s.subsetXORSum(to_test))



