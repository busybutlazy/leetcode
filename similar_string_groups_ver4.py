class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        s_l=len(strs)
        str_index=[i for i in range(len(strs))]
        l=[[] for _ in range(s_l)]
        nums_dict=dict(zip(str_index,l))
        for i in range(len(strs)):
            # for j in range(i,len(strs)):                
            for j in range(len(strs)):
                if self.is_similar(strs[i],strs[j]):
                    nums_dict[j].append(i)
        
        # print(nums_dict)
        for i in nums_dict:
            if len(nums_dict[i])==1:
                continue
            tmp=[]
            for j in nums_dict[i]:
                tmp.append(j)
            tmp_set=set()
            for j in tmp:
                tmp_set.update(set(nums_dict[j]))
            for j in tmp:
                nums_dict[j]=list(tmp_set)
        ans_list=[]
        for i in nums_dict:
            if nums_dict[i] not in ans_list:
                ans_list.append(nums_dict[i])
        return(len(ans_list))
            
            
 
    def is_similar(self,str1,str2):
        counter=0
        for i in range(len(str1)):
            if (str1[i]!=str2[i]):
                counter+=1
            if counter>2:
                return False
        # print(str1,"\n",str2,"\n","==="*30)
        return counter==2 or counter==0
    
a=Solution()
nums=["qihcochwmglyiggvsqqfgjjxu","gcgqxiysqfqugmjgwclhjhovi","gjhoggxvcqlcsyifmqgqujwhi","wqoijxciuqlyghcvjhgsqfmgg","qshcoghwmglygqgviiqfjcjxu","jgcxqfqhuyimjglgihvcqsgow","qshcoghwmggylqgviiqfjcjxu","wcoijxqiuqlyghcvjhgsqgmgf","qshcoghwmglyiqgvigqfjcjxu","qgsjggjuiyihlqcxfovchqmwg","wcoijxjiuqlyghcvqhgsqgmgf","sijgumvhqwqioclcggxgyhfjq","lhogcgfqqihjuqsyicxgwmvgj","ijhoggxvcqlcsygfmqgqujwhi","qshcojhwmglyiqgvigqfgcjxu","wcoijxqiuqlyghcvjhgsqfmgg","qshcojhwmglyiggviqqfgcjxu","lhogcgqqfihjuqsyicxgwmvgj","xscjjyfiuglqigmgqwqghcvho","lhggcgfqqihjuqsyicxgwmvoj","lhgocgfqqihjuqsyicxgwmvgj","qihcojhwmglyiggvsqqfgcjxu","ojjycmqshgglwicfqguxvihgq","sijvumghqwqioclcggxgyhfjq","gglhhifwvqgqcoyumcgjjisqx"]
a.numSimilarGroups(nums)
# print(a.is_similar(nums[12],nums[19]))