class Car:
    speed = 60
    def speedUp(self,value):
        self.speed = self.speed + value
        print('현재 속도(부모 클래스) : %d' % self.speed)
class Sedan( Car ):
    def __init__(self,value):
        self.speed = self.speed + value +20
        print('현재 속도(세단 클래스) : %d' % self.speed)
class Truck( Car ):
    def __init__(self,value):
        self.speed = self.speed + value -20
        print('현재 속도(트럭 클래스) : %d' % self.speed)

mySedan = Sedan(20)
myTruck = Truck(20)
