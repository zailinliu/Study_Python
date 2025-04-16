# # 함수를 정의한다.
# def plus(v1,v2): # v1 = 가매개변수, 인수, 파라미터터
#     result = 0
#     result = v1 + v2
#     return result

# hap = plus( 10,20 ) #함수 호출 # 10 = 실매개변수, 실인수
# print(hap)
# hap = plus(300,-500)
# print(hap)

# # 숫자3개를 함수로 보내서 큰 숫자 리턴받기
# def max_fun(a1,a2,a3):

#     return max_value
# max_v = max_fun(7,10,4)
# print(max_v)

# # 문자 2개를 함수로 보내서 길이의 합을 출력하는 함수 만들기
# def plus_len(a1, a2):
#     return len(a1)+len(a2)
# plus_v = plus_len('hello','python')
# print(plus_v)

# # 숫자 2개, 문자 1개를 함수로 보내서 숫자는 곱셉을 하고, 문자는 연산자로 보내서 리턴하기
# def fun_test(n1,n2,a):
#     if( a == '+' ):
#         result = n1 + n2
#     elif( a == '-' ):
#         result = n1 - n2
#     elif( a == '*' ):
#         result = n1 * n2
#     elif( a == '/' ):
#         result = n1 / n2
#     # print(f'{n1}{a}{n2}={result}')
#     return result
# num1 = int(input('첫번째 수는?'))
# num2 = int(input('두번째 수는?'))
# op = input('연산자(+,-,*,/)')
# # fun_test(num1,num2,op)
# test_an = fun_test(num1,num2,op)
# print(test_an)

# # 생명주기( 생성 -> 사용/처리 -> 소멸 )
# n4 = 500
# def a(n1, n2):
#     n3=100 # 함수속에서만 사용가능
#     print(n1+n2+n3+n4)
# def b(n1,n2):
#     print(n1-n2+n4)
# a(10,30)
# print(n4)
# b(100,50)

# #
# def calc_f ():
#     global n3 #전역변수
#     n3 = 100
#     print(f'{n1}{o1}{n2}{o1}{n3}')

# n1=10
# n2=20
# o1='+'
# calc_f()

# print(n3)

# # 문제2)
# global coffee
# coffee = 0
# def coffee_machine(button) :
#      print()
#      print("#1. (자동으로) 뜨거운 물을 준비한다.")
#      print("#2. (자동으로) 종이컵을 준비한다.")

#      if button == 1 :
#           print("#3. (자동으로) 아메리카노를 탄다.")
#      elif button == 2 :
#           print("#3. (자동으로) 카페라떼를 탄다.")
#      elif button == 3 :
#           print("#3. (자동으로) 카푸치노를 탄다.")
#      elif button == 4 :
#           print("#3. (자동으로) 에스프레소 탄다.")

#      print("#4. (자동으로) 물을 붓는다.")
#      print("#5. (자동으로) 스푼으로 젓는다.")
#      print()

# coffee = int(input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소소)"))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# # 실습3) %d : 정수가 들어가야할 자리
# global a
# def func1() :
#      a = 10     # 지역 변수
#      print("func1()에서 a값 %d" % a)

# def func2() :
#      print("func2()에서 a값 %d" % a)
 
# a = 20        # 전역 변수

# func1()
# func2()

# 실습4)
global a
a =20
def func1() :
     global a     # 이 함수 안에서 a는 전역 변수
     a = 10
     print("func1()에서 a값 %d" % a)

def func2() :
     print("func2()에서 a값 %d" % a)