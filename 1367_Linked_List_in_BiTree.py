from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def search_next(goal,sub_root):
            if not goal:
                return True
            if not sub_root:
                return False
            if goal.val != sub_root.val:
                return False
            return search_next(goal.next,sub_root.left) or search_next(goal.next,sub_root.right)
        
        def dfs(startpoint,subroot):
            if not subroot:
                return False
            elif subroot.val == startpoint:
                if search_next(head,subroot):
                    return True
            return dfs(startpoint,subroot.left) or dfs(startpoint,subroot.right)
        
        return dfs(head.val,root)