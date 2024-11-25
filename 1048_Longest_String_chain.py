from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) <2:return len(words)
        boxs={}
        for w in words:
            if len(w) not in boxs:
                boxs.update({len(w):[w]})
            else:
                boxs[len(w)].append(w)
        
        words.sort(key=len)
        dp={}
        
        for i,word in enumerate(words):
            if len(word)-1 not in boxs:
                dp.update({word:1})
                continue
            sub=self.make_sub(word)
            result=0
            for w in boxs[len(word)-1]:
                if w in sub and dp[w]>result:
                    result=dp[w]
            dp.update({word:result+1})
        print(dp)
        return max(dp.values())
            
    def make_sub(self,word:str):
        sub_str=set()
        for i in range(len(word)):
            sub_str.add(word[:i]+word[i+1:])
        return sub_str

s=Solution()
lsc=s.longestStrChain
words = ["a","b","aaas","ba","bca","bda","bdca"]
print(lsc(words))
