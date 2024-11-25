from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def turn (li):
            li[0],li[1]=li[1]*-1,li[0]
        
        mat=[[-1]*n for _ in range(m)]
        x,y=0,0
        direction=[1,0]

        while head:
            mat[y][x]=head.val
            next_x=x+direction[0]
            next_y=y+direction[1]
            if next_x>=0 and next_x<n and next_y>=0 and next_y<m and mat[next_y][next_x]==-1:
                x=next_x
                y=next_y
            else:
                turn(direction)
                x+=direction[0]
                y+=direction[1]
            head=head.next
        
        return mat


if __name__=="__main__":
    s=Solution()
    h=ListNode()
    tmp=h
    li=[3,0,2,6,8,1,7,9,4,2,5,5,0]
    for ele in li:
        tmp.next=ListNode(ele)
        tmp=tmp.next
    m=3
    n=5
    print(s.spiralMatrix(m,n,h.next))