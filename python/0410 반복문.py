# # 문제1)
# mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
# fruit_list = []
# number_list = []
# for i in mix_list:
#     if type(i)==str:
#         fruit_list.append(i)
#     if type(i)==int:
#           number_list.append(i)
# print( fruit_list, "str형입니다." )
# print( number_list, "int형입니다." )

# # 문제2)
# num = int(input("1이상의 정수를 입력해주세요."))
# for i in range(1,num+1,1):
#     if num%i==0:
#          print(num,'의 약수는',i, '입니다.')

# # 문제3) 
# a = [(1, 3), (5, 7), (9, 11), (13, 15)]
# for (x,y) in a:
#      print( x + y )

# # 문제4)
# name = str(input('이름을 입력해주세요: '))
# num = int(input('문제 개수를 입력해주세요: '))
# point = 0
# print('=' * 32)
# for i in range(1,num+1,1):
#     while(True):
#         print(i,'번 문제를 해결했나요? (y/n):')
#         yn = str(input())
#         if yn == 'y':
#             point += 1  
#             break
#         elif yn == 'n':
#             point += 0
#             break
#         while(True):
#             if yn != 'y''n':
#                 print('(y/n)의 형태로 다시 입력해주세요')
#                 break
# print('=' * 32)
# print(name,'학생, 총',point,'문제를 해결했습니다.')

# # 문제5)
# stock = [['시가',100,200,300],['종가',80,210,330]]

# # 문제6)
# stock = ['시가',{100,200,300},'종가',[80,210,330]]

# # 문제7)
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for n in i:
#         print(n,'호', end=" ")

# # 문제8)
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]: 
#     for n in i:
#         print(n,'호', end=" ")

# # 문제9)
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]: 
#     for n in i[::-1]:
#         print(n,'호', end=" ")

# # 문제1) 다시해보기
# mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
# mix_fruit = []
# mix_number = []
# for i in mix_list: 
#     if type(i) == str:
#         mix_fruit.append(i)
#     elif type(i) == int:
#         mix_number.append(i)
# print(mix_fruit,'는 string형 입니다.', mix_number,'는 int형입니다.')

# # 문제2) 다시해보기
# num = int(input('1이상의 정수를 입력해주세요'))
# for i in range(1,num+1,1):
#     if num%i ==0:
#         print(num,'의 약수는',i,'입니다.')
    
# # 문제3) 다시해보기
# a = [(1,3),(5,7),(9,11),(13,15)]
# for (x,y) in a:
#     print(x+y)

# # 문제4) 다시해보기
# name = str(input('이름을 입력해주세요'))
# number = int(input('문제의 개수를 입력해주세요'))
# count = 0
# print('*' * 32)

# for i in range( 1, number+1, 1 ):
#     while(True):
#         print(i,'번 문제를 해결했나요? (y/n):')
#         yn = str(input())
#         if yn == 'y':
#             count += 1
#             break
#         elif yn == 'n':
#             break
#         while(True):
#             if yn != 'y''n':
#                     print('(y/n)형식으로 다시 입력해주세요:')
#             break
# print('*' * 32)
# print(name, '학생, 총',count,'문제를 해결했습니다.')

# # 문제4) 다시해보기
# name = str(input('이름을 입력해주세요'))
# num = int(input('문제의 개수를 입력해주세요'))
# print('*' * 32)
# count = 0
# for i in range( 1, num+1, 1):
#     print(i,'번 문제를 해결했나요? (y/n):')
#     while(True):
#         yn = str(input())
#         if yn == 'y':
#             count += 1
#             break
#         elif yn == 'n':
#             break
#         while(True):
#             if yn != 'y''n':
#                 print('(y/n):의 형식으로 다시 입력해주세요')
#                 break
# print('*' * 32)
# print( name, '학생, 총', count, '문제를 해결했습니다.')

