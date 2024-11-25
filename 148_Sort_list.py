from typing import Optional
from List_Node_tool import ListNode,ListNodeTool as lnt
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map={}
        li=[]
        while head:
            hash_map[head]=head.val
            li.append(head)
            head=head.next

        li.sort(key=lambda x:hash_map[x])
        new_head=ListNode()
        tmp=new_head
        for node in li:
            tmp.next=node
            tmp=tmp.next
            tmp.next=None

        return new_head.next
    

if __name__=="__main__":
    head=lnt.node_maker([-1,5,3,4,0])
    new_head=Solution().sortList(head)
    lnt.node_printer(new_head)