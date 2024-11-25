from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.transfer_map={0:[]}
        
        
    def transfer_helper(self,k,counter):
        tmp=(counter+1)%k
        if tmp not in self.transfer_map:
            self.transfer_map.update({tmp:[i for i in range(tmp,k)]})
        return self.transfer_map[tmp]
        
        
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result=[ None for _ in range(k)]
        if head==None:return result
        set_None=[]
        counter=0
        ptr=head
        while ptr:
            print("now at ",ptr.val)
            if result[counter%k]==None:
                result[counter%k]=ptr
                set_None.append(ptr)
            else:
                for i in self.transfer_helper(k,counter):
                    set_None[i]=result[i]
                    result[i]=result[i].next
            ptr=ptr.next
            counter+=1
        for i in range(1,len(set_None)):
            set_None[i].next=None
        print("counter=",counter)
        if counter<=k:
            set_None[0].next=None    
        return result

    
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

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
k=5
nl=node_maker(head)
solution=Solution()
list_of_node=solution.splitListToParts(nl,k)
for i in range(len(list_of_node)):
    print(f"No.{i}")
    node_printer(list_of_node[i])