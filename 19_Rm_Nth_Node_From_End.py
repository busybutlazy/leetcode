from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h=ListNode(0,head)
        
        curr_node=h

        def del_node(node):
            node.next=node.next.next

        counter=0
        to_cut=h
        while curr_node:
            # print("counter=",counter)
            # print("val=",curr_node.val)
            if counter>n:
                to_cut=to_cut.next
            curr_node=curr_node.next
            counter+=1


        del_node(to_cut)

        return h.next
        





def node_maker(num_list):
    start=ListNode()
    curr_node=start
    for i in range(len(num_list)):
        curr_node.next=ListNode(num_list[i])
        curr_node=curr_node.next
    return start.next

def node_printer(node):
    while node:
        print(node.val)
        node=node.next
    

if __name__=="__main__":
    node_list=node_maker([1,2,3,4,5])
    solution=Solution()
    n=5
    node_printer(solution.removeNthFromEnd(node_list,n))