# 인스턴스 변수는 __init__ 생성자 선언 한 변수이다.
# 사용하려면 반드시 객체생성해야한다. ex) myDog = Dog()
# 사용하는 방법 myDog.in_var 
class Dog:
    c_var = "클래스변수"
    c_i_var = 100

    def __init__(self):
        self.in_var = "인스턴스 변수"
        self.in_i = 200
classDog = Dog()
print(classDog.c_var, classDog.c_i_var)
print(classDog.in_var,classDog.in_i)
print(Dog.c_var,Dog.c_i_var)
print(Dog.in_var,Dog.in_i)