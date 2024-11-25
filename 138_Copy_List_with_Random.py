from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step by step solution
        if head==None:return None
        map_of_nodes={}
        # old node : new node
        ptr=head
        while ptr:
            map_of_nodes.update({ptr:Node(ptr.val)})
            ptr = ptr.next
        ptr=head
        while ptr:
            if ptr.next:
                map_of_nodes[ptr].next=map_of_nodes[ptr.next]
            if ptr.random:
                map_of_nodes[ptr].random=map_of_nodes[ptr.random]
            ptr=ptr.next
        return map_of_nodes[head]
        pass
        # Interweaving node
        

            

solution=Solution()

def check_ans(n):
    while n:
        print(n.val)
        n=n.next

n4=Node(1)
n3=Node(10,next=n4)
n2=Node(11,next=n3,random=n4)
n1=Node(13,next=n2)
n0=Node(7,next=n1,random=None)
n4.random=n0
n3.random=n2
n1.random=n0
check_ans(n0)
check_ans(solution.copyRandomList(n0))