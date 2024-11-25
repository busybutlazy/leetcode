class MyHashSet:

    def __init__(self):
        self.box = set()
        pass

    def add(self, key: int) -> None:
        self.box.add(key)
        pass

    def remove(self, key: int) -> None:
        if key in self.box:
            self.box.remove(key)
        pass

    def contains(self, key: int) -> bool:
        return key in self.box
        
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
param_3 = obj.contains(1)
print(param_3)
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
