class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class ListNodeTool:
    def node_maker(input_list:list)->ListNode:
        if type(input_list)!=list or len(input_list)<1:
            print("Step:node_maker. Worng input!!!")
            return False
        head=ListNode()
        tmp=head
        for ele in input_list:
            tmp.next=ListNode(val=ele)
            tmp=tmp.next
        
        return head.next
    
    def node_printer(head:ListNode)->None:
        tmp=head
        while tmp:
            print(tmp.val)
            tmp=tmp.next


if __name__=="__main__":
    lnt=ListNodeTool
    lnt.node_printer(lnt.node_maker([2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]))