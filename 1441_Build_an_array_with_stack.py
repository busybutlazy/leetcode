from typing import List

class Stack:
    def __init__(self):
        self.result=[]
        self.stream=1
    
    def push(self):
        self.result.append(self.stream)
        self.stream+=1
    
    def pop(self):
        self.result=self.result[:-1]
            



class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=Stack()
        for i in range(1,n+1):
            stack.push()
            if i not in target:
                stack.pop()
        return stack.result
    
s=Solution()
print(s.buildArray([1,3],3))
            
                
            