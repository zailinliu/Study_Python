# # 문제11)
# def quiz(answer , eng):
#     if( answer == eng ):
#         print('정답입니다.')
#     else:
#         print('틀렸습니다.')

# eng_dict = {"house":"집",  "piano":"피아노",  "christmas":"크리스마스",  "friend":"친구", "bread":"빵" }
# for eng in eng_dict.keys():
#     answer = input( eng_dict[eng] + "의 영어 단어는? : ")
#     quiz( answer, eng )

# # 문제10)
# def cnt(sent, alphabet):
#     cnt = 0
#     for i in sent : 
#         if i == alphabet:
#             cnt += 1
#     return cnt

# sent = input('영어문장을 입력하세요:')
# alphabet = input('알파벳하나를 입력하세요:')

# result = cnt( sent, alphabet )
# print(sent,'에 포함된',alphabet,'의 개수는',result,'개 입니다.')

# 문제9)
def mile(km):
    mile = km * 0.621371
    return mile

km = int(input('km를 입력하세요.'))
result = mile(km)

print(km,'km는',result,'mile입니다.')