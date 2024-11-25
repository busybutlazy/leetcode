from typing import List
from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.n2c=defaultdict()
        def make_list(li:List,num:str):
            new_list=[]
            for strs in li:
                for c in self.n2c[num]:
                    new_list.append(strs+c)
            return new_list
        
        
        
        result=[]
        for i in range(len(digits)):
            if digits[i] not in self.n2c:
                if digits[i]=="7":
                    self.n2c["7"]=["p","q","r","s"]
                elif digits[i]=="8":
                    self.n2c["8"]=["t","u","v"]
                elif digits[i]=="9":
                    self.n2c["9"]=["w","x","y","z"]
                else:
                    self.n2c[digits[i]]=[chr(int(digits[i])*3+91),chr(int(digits[i])*3+92),chr(int(digits[i])*3+93)]
            if i == 0:
                result=self.n2c[digits[i]]
            else:
                result=make_list(result,digits[i])
    
        return result
    
s=Solution()
digits="7"
print(s.letterCombinations(digits))
            
