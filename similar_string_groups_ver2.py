class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        self.groups=[]
        for s in strs:
            self.in_group(s)
        print(self.groups)
        
    def in_group(self,s):
        for group in self.groups:
            for ss in group:
                if self.is_similar(s,ss):
                    group.append(s)
                    return
        self.groups.append([s])
                
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
a.numSimilarGroups(nums)