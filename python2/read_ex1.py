# # 요구사항 - data1.txt 파일을 읽어서 화면 출력하기
# inF = None # 자료형이 무엇인지 아직 정해지지 않았다.
# inF = open ("./python2/temp/data1.txt" , "r", encoding="utf-8")
# while(True):
#     instr = inF.readline()
#     if instr == "": # 참이면 EOF(파일의 끝) 이다.
#         break
#     else:
#         print(instr)
# inF.close() # 자원반납

# # data2 파일을 읽어서 화면 출력하기
# inF = open("./python2/temp/data2.txt" , "r" , encoding="utf-8")
# while(True):
#     instr = inF.readline()
#     if instr == "":
#         break
#     else:
#         print(instr)
# inF.close()

# # 문제1) 
# inF = None
# instr = ""
# inF = open("./python2/temp/data.txt" , "r")
# while(True):
#     instr = inF.read()
#     if instr == "":
#         break
#     else:
#         print(instr)
# inF.close()

# # 문제2)
# inF = None
# instr = ""
# inF = open("./python2/temp/data_utf8.txt" , "r", encoding="utf-8")
# while(True):
#     instr = inF.readline()
#     if instr == "":
#         break
#     else :
#        print(instr)
# inF.close()

# # 문제3)
# f= input('파일명을 입력하세요: ')
# with open(f, "r") as inF:
#     instr = inF.readlines()
#     print

# 문제4)
import os

inF = None
fName,inList,inStr = "",[],""
while(True):
    fName = input('파일명을 입력하세요 : ')
    if os.path.exists(fName):
        with open(fName,"r",encoding="utf-8") as inF:
            inList = inF.readlines()
        for inStr in inList:
            print(inStr)   
            break     
    else:
        print("%s 파일이 없습니다." %fName)