# g_var = '홍길동'
# def func():
#     result = 100
#     return result

# def func2():
#     result = 200
#     print(result, g_var,point)

# def func3():
#     global point # => global은 특정함수내에 써도 전역변수가 된다. 
#     point = 100
#     r = 10
#     r1 = 20
#     r_list = [ r, r1 ]
#     print (r_list)
#     return r_list
# # 함수에서 2개 값을 반환하게 하기(X)
# # 함수에서 return은 한개만 가능하다

# def func4(n1,n2,n3):
#     result = n1+n2+n3
#     return result
# def func4(n1,n2 = 50):
#     result = 0
#     result = n1+n2
#     print(n1,n2)
#     return result

# print(func4( 100,200 ))
# # 파이썬에서는 함수오버로딩이 안됌. * 마지막 함수만 남고, 위에 함수들은 기능X

# func3()

# print(func())
# hap = func()
# print(hap)
# func2()

# def para_func( *para ): # (10,20,30,40)
#     result = 0 # 지역변수
#     for i in para:
#         result += i
#     return result

# hap = 0 # 전역변수
# hap = para_func( *range(1, 101, 1) ) # 함수호출
# print( hap )

# # 최댓값 구하기기
# def para_func( *para ): # (10,20,30,40)
#     max = para[0][0]
#     for i in para:
#         for num in i:
#             if max < num:
#                 max = num
#     return max

# max = 0 # 전역변수
# a = tuple(range( 1, 101, 1 ))
# a_data = (10,-20,50,80,200,-30)
# max = para_func( a_data )
# print( max )

# # 최소값 구하기기
# def para_func( *para ): # (10,20,30,40)
#     min = para[0][0]
#     for i in para:
#         for num in i:
#             if min > num:
#                 min = num
#     return min

# min = 0 # 전역변수
# a = tuple(range( 1, 101, 1 ))
# a_data = (10,-20,50,80,200,-30)
# min = para_func( a_data )
# print( min )

# def dic_func( **para ) :
#     print(para)
#     for k in para.keys():
#         print((k,para[k]))
# dic_func( 심화반점수 =  [100,25,30] )

# # 심화반 점수의 합계를 구하기
# def dic_func( **para ) :
#     print(para)
#     for k in para.keys():
#         sum = 0
#         for score in para[k]:
#             sum += score
#         print("%s --> %d" %(k,sum),)
# dic_func( 심화반점수의합계 =  [100,75,80] , 기초반점수 = [80,90,100,50,80] )

# # 문제1)
# def area( width, height ) :
#     area = width * height / 2
#     return area

# width_value = int(input('삼각형의 너비를 입력해주세요.'))
# height_value = int(input('삼각형의 높이이를 입력해주세요.'))

# print('삼각형의 면적은 :', area(width_value,height_value) ,'입니다.')

# 문제2)
num = int(input('1~100까지의 정수를 입력해주세요:'))
result = 0
for i in range(1,101,1):
    if i % num ==0:
        result += i
        
print(result)
# 문제2) => 함수형으로
def sum_num( num ):
    

num = int(input('1~100까지의 정수를 입력해주세요:'))
result = 0
for i in range(1,101,1):
    if i % num ==0:
        result += i
        
print(result)


# # 문제3)
# space