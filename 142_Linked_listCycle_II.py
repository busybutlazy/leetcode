from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []
        ptr=head
        while ptr.next :
            if ptr.next in visited:
                return ptr
            ptr =ptr.next
            visited.append(ptr)
        return None
n0=ListNode(3)
n1=ListNode(2)
n2=ListNode(0)
n3=ListNode(-4)

n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n1

solution=Solution()
print(solution.detectCycle(n0).next.val)