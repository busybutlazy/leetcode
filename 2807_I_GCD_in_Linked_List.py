from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front=head
        if front.next:
            back=front.next
        else:
            return front
        
        def find_GCD(n1,n2):
            if n2>=n1:
                n1,n2=n2,n1
            if n1==n2:
                return n1
            else:
                n1=n1-n2
                return find_GCD(n1,n2)

        while front and back:
            gcd=find_GCD(front.val,back.val)
            front.next=ListNode(gcd,back)
            front=back
            back=back.next

        return head

