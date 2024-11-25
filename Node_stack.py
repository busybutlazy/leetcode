class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node_Stack():
    """
    __init__(input_list:list,maximum:int=100):\n
        input_list: Elements to push.\n
        maximum: Limit of the stack.\n
    push(val)->None: Add an element to the stack.\n
    pop( ): Pop the top element to the stack\n
    """
    
    def __init__(self,input_list:list,maximum:int=100):
        # if len(input_list)==0:
        #     raise Exception("Length of input_list must bigger than 0.")
        
        self.__Maximum=maximum
        self.__length=0
        self.__node=Node(None)
        for i in range(len(input_list)-1,-1,-1):
            self.push(input_list[i])
    
    def push(self,val)->None:
        if self.__length>=self.__Maximum:
                raise Exception("Run out of stack. Please creat a larger stack.")
        new_head=Node(val)
        new_head.next=self.__node
        self.__node=new_head
        self.__length+=1


    def pop(self,log:bool=False):
        if self.__node.val==None and self.__node.next==None:
            if log!=False:
                print("End of the stack.")            
            output=None
        else:
            self.__length-=1
            if log!=False:
                print(f"The length of rest stack is {self.__length}")
            output=self.__node.val
            self.__node=self.__node.next
            return output

    def __len__(self)->int:
        return self.__length
    
    


if __name__=="__main__":
    li=[3,3,5,0,6]
    ns=Node_Stack(li)
    ns.push(2)
    ns.push(1)
    print(len(ns))
    output=ns.pop()
    while output!=None:
        print(output)
        output=ns.pop()
