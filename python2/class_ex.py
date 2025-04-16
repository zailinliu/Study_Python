# 1단계 설계한다.
# 2단계 인스턴스(객체)화 한다. : 메모리(RAM의 힙 메모리)에 올린다.
# 3단계 변수에 값을 넣기, 함수를 호출,출력하기
class Car :
    color = ""   # flid : class 안에 선언한 변수
    speed = 0    
    # method : class 안에 선언한 함수
    def speedUp (self, value) :  # self : 자기자신신
        self.speed = self.speed + value
    def speedDown (self,value) :
        self.speed = self.speed - value
 
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 350
myCar2 = Car()
myCar2.color = "white"
myCar2.speed = 100
myCar3 = Car()
myCar3.color = "black"
myCar3.speed = 300

myCar1.speedDown(150)
myCar2.speedUp(70)
myCar3.speedDown(90)
print('myCar1의 색상은 %s 이며, 현재속도는 %dkm입니다.' % (myCar1.color,myCar1.speed))
print('myCar2의 색상은 %s 이며, 현재속도는 %dkm입니다.' % (myCar2.color,myCar2.speed))
print('myCar3의 색상은 %s 이며, 현재속도는 %dkm입니다.' % (myCar3.color,myCar3.speed)) 

class Bus :
    color = ""
    speed = 0

    def __init__(self,value1,value2):
        self.color = value1
        self.speed = value2

    def speedUp(self,value) :
        self.speed += value
    
    def speedDown(self,value) :
        self.speed -= value

myBus1 = Bus("red",80)
myBus2 = Bus("black",100)

print('myBus1의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myBus1.color,myBus1.speed))
print('myBus2의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myBus2.color,myBus2.speed))