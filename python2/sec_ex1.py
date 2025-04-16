# print(ord('파')) # ord('문자') => 문자의 유니코드값 반환
# num = ord('파')
# print(chr(num))

# aa = chr( num - 419 )

# num = ord(aa)
# print (chr(num + 419))

inF, outF = None, None
inStr, outStr = "",""
i = 0
secu = 0

secuYN = input("1.암호화 2.암호해석  선택")
inFname = input('입력 파일명은? :')
outFname = input('출력 파일명은? :')

if (secuYN == '1'):
    secu = 419
elif (secuYN == '2'):
    secu = -419
inF = open(inFname, 'r', encoding = 'utf-8')
outF = open(outFname, 'w', encoding = 'utf-8')
while(True):
    inStr = inF.readline()
    if not inStr:
        break
    outStr = ""
    for i in range(0,len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr( chNum )
        outStr = outStr + ch2
    outF.write(outStr)
outF.close()
inF.close()
print(' %s --> %s 변환 완료' % (inFname, outFname))

