from typing import Optional,List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.map=defaultdict()
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def helper(n:int,ptr:TreeNode):
            if ptr.val:
                if n not in self.map:
                    self.map[n] = [ptr.val]
                else:
                    self.map[n].append(ptr.val)
            if ptr.left:
                helper(n+1,ptr.left)
            if ptr.right:
                helper(n+1,ptr.right)
        helper(0,root)
        return [max(self.map[i]) for i in range(len(self.map))]
        
    


def build_TreeNode(list_of_nums):
    n=0
    node_list=[TreeNode(num) for num in list_of_nums]
    while (n*2)+2<len(list_of_nums):
        node_list[n].left=node_list[n*2+1]
        node_list[n].right=node_list[n*2+2]
        n+=1
    return node_list[0]

def print_tree(node):
    print(node.val)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)

root=[1,3,2,5,3,None,9]
head=build_TreeNode(root)
# print_tree(head)

s=Solution()
print(s.largestValues(head))