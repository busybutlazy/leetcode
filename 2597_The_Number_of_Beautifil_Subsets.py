class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if len(nums)==1:
            return 1
        
        self.nums=nums
        self.black_map={}
        self.result=0
        for i in range(len(nums)):
            if nums[i] not in self.black_map:
                    self.black_map.update({nums[i]:[]})
            for j in range(i+1,len(nums)):
                if nums[j] not in self.black_map:
                    self.black_map.update({nums[j]:[]})
                if nums[i]-nums[j]!=k and nums[j]-nums[i]!=k:
                    continue
                self.black_map[nums[i]].append(nums[j])
                self.black_map[nums[j]].append(nums[i])
        for i in range(len(nums)):
            self.recursive(i,[])

        return self.result
        

    def recursive(self,index,ban_list):        
        if self.nums[index] not in ban_list:
            self.result+=1
            print("plus 1")
            ban_list=ban_list+self.black_map[self.nums[index]]
        
        print("result=",self.result)
        if index==len(self.nums)-1:
            print("end of tail")
            return

        for i in range(index+1,len(self.nums)):
            if self.nums[i] not in ban_list:
                self.recursive(i,ban_list)





if __name__=="__main__":
    n=Solution()
    to_test=[9,5,7,10,6,2]
    print(n.beautifulSubsets(to_test,9))



        # result=[[nums[0]]]
        # for i in range(1,len(nums)):
        #     to_add=[]
        #     for ele in result:
        #         if ele[-1]-nums[i]==k or nums[i]-ele[-1]==k:
        #             continue
        #         to_add.append(ele+[nums[i]])
        #     if len(to_add)!=0:
        #         result=result+to_add
        #     result.append([nums[i]])
        # return len(result)
        # num_map={}
        # for i in range(len(nums)):
        #     print("i=",i,"  num_map=",num_map)
        #     num_map.update({nums[i]:1})
        #     for j in range(i):
        #         if nums[i]-nums[j]!=k and nums[j]-nums[i]!=k:
        #             num_map[nums[i]]+=2*num_map[nums[j]]
        # return num_map