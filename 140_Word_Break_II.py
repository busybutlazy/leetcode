from typing import List
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.capital_dict=defaultdict(list)
        self.answer:List[str]=[]
        for word in wordDict:
            self.capital_dict[word[0]].append(word)
        
        self.recursive(s,"")
        
        return self.answer
    
    def recursive(self,left_s:str,now_answer:str):
        if len(left_s)==0:
            self.answer.append(now_answer[:-1])
            return
        if left_s[0] not in self.capital_dict:
            return
        for word in self.capital_dict[left_s[0]]:
            if word==left_s[:len(word)]:
                self.recursive(left_s[len(word):],now_answer+word+" ")
    
        
    
if __name__ == '__main__':
    solution=Solution()
    s = "catsanddogcatsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(solution.wordBreak(s,wordDict))