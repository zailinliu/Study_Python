# myStr = '파이썬은 재미있어요. 파이썬 예외처리 공부'
# strPosList = [] 
# index = 0

# while(True):
#     try:
#         index = myStr.index('파이썬',index)
#         strPosList.append(index)
#         index = index + 1
#     except :
#         print('없는자료입니다.')
#         break
# print('파이썬의 글자 위치 --->', strPosList)

num1 = input('숫자 1을 입력해주세요: ')
num2 = input('숫자 2를 입력해주세요: ')
try:
    num1 = int(num1)
    num2 = int(num2)
    res = num1 / num2
    print('결과는: ' , res)
# except ZeroDivisionError: 
#     num2 = input('0으로 나누려고 시도했습니다. 숫자2를 다시 입력하세요: ')
#     res = num1 / int(num2)
#     print('결과는: ', res)
# except TypeError:
#     print('자료형을 정수형으로 입력하세요: ')
# except :
#     print('에러가 발생했어요.')
except Exception as e:
    print(type(e).__name__, '에러가 났습니다.')

# while(True):
#     num1 = input('숫자 1: ')
#     num2 = input('숫자 2: ')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         if (num2 == 0) :
#             print('나누는 수가 0이므로 다시 입력해주세요: ')
#             continue #반복문의 처음으로
#         else :
#             res = num1 / num2
#             print('결과는' , res)
#             break
#     except:
#         print('예외처리')
#         break