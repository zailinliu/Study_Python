# class에서 생성자의 가매개변수의 개수를 유동적으로 하려면 *매개변수 - tuple형식으로 저장됨 , **매개변수 - dict 형식으로 저장됨

class Car:
    color =  ""
    price = 0
    speed = 0
    # 생성자 : 객체생성 Car() 할 때 자동으로 호출된 곳
    def __init__(self, *v1):
        for i in range(len(v1)):
            if (i == 0):
                self.color = v1[0]
            if (i == 1):
                self.price = v1[1]
            if (i == 2):
                self.speed = v1[2]

myCar = Car("red", 80000000, 30)
print ('color :', myCar.color,', price:', myCar.price,'$',', speed: ',myCar.speed)
myCar2 = Car("blue", 60000000)
print ('color :', myCar2.color,', price:', myCar2.price,'$',', speed: ',myCar2.speed)
myCar3 = Car("black")
print ('color :', myCar3.color,', price:', myCar3.price,'$',', speed: ',myCar3.speed)