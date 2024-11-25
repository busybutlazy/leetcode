class SeatManager:

    def __init__(self, n: int):
        self.itr=1
        self.ret =[]
    def reserve(self) -> int:
        if len(self.ret)==0:
            to_send=self.itr
            self.itr+=1
            return self.itr
        return self.ret.pop()

    def unreserve(self, seatNumber: int) -> None:
        self.ret.append(seatNumber)
        self.ret.sort()


s=SeatManager(798)
print(s.reserve())
print(s.unreserve(1))
print(s.reserve())
print(s.unreserve(1))
print(s.reserve())
