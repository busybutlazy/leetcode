from collections import deque

class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        tmp=self.li[-1]
        self.li=self.li[:-1]
        return tmp
    
    def top(self) -> int:
        return self.li[-1]

    def empty(self) -> bool:
        if len(self.li)==0:return True
        return False

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2,param_3,param_4)