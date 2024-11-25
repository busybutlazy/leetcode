class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_len=len(nums)
        result=[[]]
        for i in range(num_len):
            if len(result)==1:
                result.append([nums[i]])
            else:
                to_add=[]
                for ele in result: 
                    to_add.append(ele+[nums[i]])
                result=result+to_add
        return result




if __name__=="__main__":
    n=Solution()
    to_test=[0,3,5,7,9]
    print(n.subsets(to_test))


