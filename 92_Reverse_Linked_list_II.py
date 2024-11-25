from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head
        ptr=head
        location=[]
        while ptr:
            location.append(ptr)
            ptr=ptr.next
        new_order=[i for i in range(0,left-1)]+[i for i in range(right-1,left-2,-1)]+[i for i in range(right,len(location))]
        print(new_order)
        new_head=location[new_order.pop(0)]
        ptr=new_head
        for i in new_order:
            ptr.next=location[i]
            ptr=ptr.next
        ptr.next=None
        return new_head
        


def node_maker(vals: List[int]):
    head=None
    for i in range(len(vals)-1,-1,-1):
        head=ListNode(vals[i],head)
    return head

def node_printer(head: Optional[ListNode]):
    while head:
        print(head.val,end=",")
        head=head.next
    print("")

    

head = [1,2]
left = 1
right = 2
head=node_maker(head)
node_printer(head)
s=Solution()
new_head=s.reverseBetween(head,left,right)
node_printer(new_head)