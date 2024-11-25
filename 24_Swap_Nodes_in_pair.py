from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        previous_node=ListNode(-100,head)
        new_head=previous_node
        node1,node2=head,head.next

        while node1 and node2:
            tail_node=node2.next
            previous_node.next=node2
            node2.next=node1
            node1.next=tail_node

            previous_node=node1
            if node1.next:
                node1=node1.next
                node2=node1.next
            else:
                break

        return new_head.next
