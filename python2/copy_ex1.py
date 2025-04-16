# inF, outF = None, None
# inStr = ""

# inF = open("./python2/temp/eric.jpg" , "rb")
# outF = open("./python2/temp/copy_emg1.jpg" , "wb")

# while(True):
#     i = inF.read()
#     if ( i == "" ):
#         break
#     else:
#         outF.write(i)
# inF.close()
# outF.close()

# # gif 파일 복사
# inF, outF = None, None
# inStr = ""

# inF = open("./python2/temp/css.gif" , "rb")
# outF = open("./python2/temp/copy_css2.gif" , "wb")

# for i in inF.readlines():
#     outF.write(i)
# inF.close()
# outF.close()

# 문제2)
inF,outF = None,None
inStr = ""

socF = input("소스 파일명을 입력하세요: ")
tarF = input("타깃 파일명을 입력하세요: ")

inF = open(socF,"rb")
outF = open(tarF,"wb")
for i in inF.readlines():
    outF.write(i)
inF.close()
outF.close()