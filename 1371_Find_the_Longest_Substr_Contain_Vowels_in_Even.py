class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        self.max_length=0
        self.vowels="aeiou"
        self.helper(s)
        return self.max_length

    def helper(self,subarr:str):
        check_list={"a":True,"e":True,"i":True,"o":True,"u":True}
        flag=True
        for i in range(len(self.vowels)):
            if subarr.count(self.vowels[i])%2!=0:
                check_list[self.vowels[i]]=False
                flag=False

    

if __name__=="__main__":
    sol=Solution()
    s="leetcodeisgreat"
    print(sol.findTheLongestSubstring(s))