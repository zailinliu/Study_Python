try:
    inF = None
    inF = open("./temp/data2.txt", "r",encoding="utf-8")
except FileNotFoundError:
    print('파일이 없습니다.')
else :
    inList = inF.readlines()
    print(inList)
finally :
    if (inF != None):
        inF.close()