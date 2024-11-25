class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        nums=len(strs)
        set_list=[]
        for index_now in range(nums):
            s_list=[]
            # print(strs[index_now],end="")
            s_list.append(strs[index_now])
            for i in range(index_now+1,nums):
                if self.is_similar(strs[index_now],strs[i]):
                    s_list.append(strs[i])
            self.check_exist(set_list,s_list)
        print(set_list)
        for s in strs:
            tmp=[]
            for i in range(len(set_list)):
                if s in i:
                    tmp.append(i)
            if(len(tmp)>1):
                for nums in set_list:
                    new_set=[]
                    new_set.append()
        return(len(set_list))

    def check_exist(self,set_list,s_list):
        for num_list in set_list:    
            for s in s_list:
                if s in num_list:
                    num_list+=s_list
                    num_set=set(num_list)
                    num_list=list(num_set)
                    return
        set_list.append(s_list)
                
    def is_similar(self,str1,str2):
        counter=0
        for i in range(len(str1)):
            if (str1[i]!=str2[i]):
                counter+=1
            if(counter>2):
                return False
        return True

nums=["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"]
a=Solution()
print(a.numSimilarGroups(nums))