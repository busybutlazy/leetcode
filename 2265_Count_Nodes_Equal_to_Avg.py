from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(ptr:TreeNode)->(int,int,int):
            count=0
            n=1
            curr_sum=ptr.val
            if ptr.left!=None:
                to_count,to_sum,to_n=helper(ptr.left)
                curr_sum+=to_sum
                n+=to_n
                count+=to_count
            if ptr.right!=None:
                to_count,to_sum,to_n=helper(ptr.right)
                curr_sum+=to_sum
                n+=to_n
                count+=to_count
            if curr_sum//n==ptr.val:
                count+=1
            return count,curr_sum,n
        return helper(root)[0]
            
