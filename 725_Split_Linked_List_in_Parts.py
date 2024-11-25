from typing import Optional,List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counter=0
        
        tmp=head
        while tmp:
            counter+=1
            tmp=tmp.next
        record=[(counter//k)+1]*(counter%k)+[counter//k]*(k-counter%k)
        result=[None]*k
        tmp=head

        for i in range(len(record)):
            result[i]=tmp
            if record[i]==0:
                break
            c= record[i]
            while c>1:
                tmp = tmp.next
                c-=1
            tmp2=tmp.next
            tmp.next=None
            tmp=tmp2

        return result

s=Solution()
li=[1,2,3,4,5,6,7,8]
head=ListNode(0)
tmp=head
for i in range(len(li)):
    tmp.next=ListNode(li[i])
    tmp=tmp.next
ans=s.splitListToParts(head,5)

for i in range(len(ans)):
    print(f"this is section {i}")  
    while ans[i]:
        print(ans[i].val,end="")
        ans[i]=ans[i].next  
    print("")