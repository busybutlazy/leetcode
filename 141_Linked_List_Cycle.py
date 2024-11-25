from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited=[]
        # visited.append(head[0])
        # ptr=head[0]
        # while ptr:
        #     if ptr.next in visited:
        #         return True
        #     visited.append(ptr.next)
        #     ptr=ptr.next
        # return False
        fast_pointer=head.next
        slow_pointer=head
        
        while (fast_pointer and fast_pointer.next):
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
            if slow_pointer==fast_pointer:
                return True
        return False
        
        
        
    
n0=ListNode(3)
n1=ListNode(2)
n2=ListNode(0)
n3=ListNode(-4)

n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n1

solution=Solution()
print(solution.hasCycle(n0))