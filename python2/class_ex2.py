class Person:
    name = ""
    age = 0
    address = ""
    def __init__(self,*args,**kwargs):
        if args :
            self.name = args[0]
            self.age = args[1]
            self.address = args[2]
        if kwargs :
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.address = kwargs["address"]
p1 = Person('홍길동', 20, '성남시') 
print(p1.name, p1.age, p1.address) 
p2 = Person(name='이순신',age=30,address='서울시') # 실인수 값이 key=value의 형태 : dict
print(p2.name, p2.age,p2.address) 
p3 = Person()
print(p3.name, p3.age,p3.address)