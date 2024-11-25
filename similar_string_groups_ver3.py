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
            for j in range(i+1,len(strs)):
                if self.is_similar(strs[i],strs[j]):
                    nums_dict[j].append(i)
        print(nums_dict)
        # for i in nums_dict:
        #     print(nums_dict[i])
        
        sum=s_l
        # print(nums_dict.values)
        for i in range(s_l):
            for j in nums_dict:
                if i in nums_dict[j]:
                    sum-=1
        print(sum)
                    
        
        
        
        
    def is_similar(self,str1,str2):
        counter=0
        for i in range(len(str1)):
            if (str1[i]!=str2[i]):
                counter+=1
            if counter>2:
                return False
        print(str1,"\n",str2,"\n","==="*30)
        return counter==2 or counter==0
    
# nums=["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"]
a=Solution()
nums=["qihcochwmglyiggvsqqfgjjxu","gcgqxiysqfqugmjgwclhjhovi","gjhoggxvcqlcsyifmqgqujwhi","wqoijxciuqlyghcvjhgsqfmgg","qshcoghwmglygqgviiqfjcjxu","jgcxqfqhuyimjglgihvcqsgow","qshcoghwmggylqgviiqfjcjxu","wcoijxqiuqlyghcvjhgsqgmgf","qshcoghwmglyiqgvigqfjcjxu","qgsjggjuiyihlqcxfovchqmwg","wcoijxjiuqlyghcvqhgsqgmgf","sijgumvhqwqioclcggxgyhfjq","lhogcgfqqihjuqsyicxgwmvgj","ijhoggxvcqlcsygfmqgqujwhi","qshcojhwmglyiqgvigqfgcjxu","wcoijxqiuqlyghcvjhgsqfmgg","qshcojhwmglyiggviqqfgcjxu","lhogcgqqfihjuqsyicxgwmvgj","xscjjyfiuglqigmgqwqghcvho","lhggcgfqqihjuqsyicxgwmvoj","lhgocgfqqihjuqsyicxgwmvgj","qihcojhwmglyiggvsqqfgcjxu","ojjycmqshgglwicfqguxvihgq","sijvumghqwqioclcggxgyhfjq","gglhhifwvqgqcoyumcgjjisqx"]
a.numSimilarGroups(nums)
# print(a.is_similar(nums[12],nums[19]))