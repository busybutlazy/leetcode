from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=s2=""
        while l1:
            s1=str(l1.val)+s1
            l1=l1.next
        while l2:
            s2=str(l2.val)+s2
            l2=l2.next
        total=str(int(s1)+int(s2))
        
        head=ListNode()
        tmp=head
        for i in range(len(total)-1,-1,-1):
                tmp.next=ListNode(total[i])
                tmp=tmp.next
        return head.next  
            
        
            
    

# l1=ListNode(2,ListNode(4,ListNode(3)))
# l2=ListNode(5,ListNode(6,ListNode(4)))
# l1=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
# l2=ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
l1=ListNode(2,ListNode(4,ListNode(9)))
l2=ListNode(5,ListNode(6,ListNode(4,ListNode(9))))
r=Solution().addTwoNumbers(l1,l2)
while r:
    print(r.val)
    r=r.next
