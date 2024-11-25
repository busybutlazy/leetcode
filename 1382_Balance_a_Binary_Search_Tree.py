# Definition for a binary tree node.
from typing import List
from TreeNode_tool import TreeNode,tree_maker,tree_to_list
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def get_TN_list(subroot):
            if subroot==None:
                return []
            else:
                return get_TN_list(subroot.left)+[subroot]+get_TN_list(subroot.right)
        TN_list=get_TN_list(root)
        
        def built_bst(list_of_tn):
            if not list_of_tn: 
                return None
            mid= len(list_of_tn)//2
            list_of_tn[mid].left=built_bst(list_of_tn[:mid])

            list_of_tn[mid].right=built_bst(list_of_tn[mid+1:])
            return list_of_tn[mid]

        return built_bst(TN_list)


if __name__=="__main__":
    root = tree_maker([1,None,2,None,None,None,3,None,None,None,None,None,None,None,4])
    result=Solution().balanceBST(root)
    print(tree_to_list(result))
