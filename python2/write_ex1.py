# outF = None
# outStr = ""
# outF = open("./python2/temp/output2.txt", "a",encoding="utf-8")
# while(True):
#     outStr = input('저장할 내용을 키보드로 입력하세요: ')
#     if outStr != "":
#         outF.writelines(outStr + "\n")
#     else:
#         break
# outF.close()
# print('파일이 저장되었습니다.')

# 문제1)
outF = None
outStr = ""
fName = input('출력할 파일경로를 입력하세요: ')
outF = open(fName, "a",encoding="utf-8")
while(True):
    outStr = input('저장할 내용을 키보드로 입력하세요: ')
    if outStr != "":
        outF.writelines(outStr + "\n")
    else:
        break
outF.close()
print('파일이 저장되었습니다.')