from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        elements =set(leftChild+rightChild)
        if len(elements)!=n: return False
        
        head=0
        for i in range(n):
            if i not in elements:
                head=i
        self.leftChild=leftChild
        self.rightChild=rightChild
        self.done=set()
        self.checker=True
        self.run_tree(head)
        
        if len(self.done)!=n:return False
        return self.checker
        
        
    
    def run_tree(self,index):
        if index in self.done:
            self.checker=False
            return
        else:
            self.done.add(index)
        if self.leftChild[index]!=-1:
            self.run_tree(self.leftChild[index])
        if self.rightChild[index]!=-1:
            self.run_tree(self.rightChild[index])
        return
        
        
s=Solution()
n = 4
leftChild = [3,-1,1,-1]
rightChild =[-1,-1,0,-1]
print(s.validateBinaryTreeNodes(n,leftChild,rightChild))