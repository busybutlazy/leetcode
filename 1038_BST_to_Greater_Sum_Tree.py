from TreeNode_tool import TreeNode ,tree_maker,tree_to_list
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def find_sum(root):
            if root==None:
                return 0
            
            val=root.val if root.val else 0
            return find_sum(root.left)+val+find_sum(root.right)
        
        self.sum_of_tree=find_sum(root)
        def change_num(root):
            if root==None:
                return
            change_num(root.left)
            if root.val!=None:
                root.val,self.sum_of_tree=self.sum_of_tree,self.sum_of_tree-root.val
            change_num(root.right)

        change_num(root)

        return root        
    
if __name__=="__main__":
    root=tree_maker([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    
    result=Solution().bstToGst(root)

    print(tree_to_list(result))