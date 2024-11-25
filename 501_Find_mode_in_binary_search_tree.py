from typing import List, Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dict=defaultdict(int)
        
        def count(value):
            if value not in self.dict:
                self.dict[value]=1
            else:
                self.dict[value]+=1
        
        def search(root: Optional[TreeNode]):
            count(root.val)
            if root.left:
                search(root.left)
            if root.right:
                search(root.right)
        result=[]
        for key in self.dict:
            if self.dict[key]==max(list(self.dict.items)):
                result.append(key)
        return result
    
    