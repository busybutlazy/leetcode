from typing import Optional
from TreeNode_tool import tree_maker,tree_printer

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.step=0
        self.step_counter(root)
        return self.step

    def step_counter(self,root):
        if not root:
            return 0
        
        l_sum=self.step_counter(root.left)
        r_sum=self.step_counter(root.right)
        print("now val=",root.val)

        print("l_sum=",l_sum,"  r_sum=",r_sum)

        self.step+=abs(l_sum)+abs(r_sum)
        return l_sum+r_sum+root.val-1

if __name__=="__main__":
    solution=Solution()
    root=tree_maker([0,1,1,4,0,1,0])
    print(solution.distributeCoins(root))