class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_space={1:big,2:medium,3:small}

    def addCar(self, carType: int) -> bool:
        if self.car_space[carType]>0:
            self.car_space[carType]-=1
            return True
        return False
            


ps=ParkingSystem(1,1,0)
car_list=[1,2,3,1]
for _ in range(len(car_list)):
    tmp=car_list.pop(0)
    print(ps.addCar(tmp))
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)