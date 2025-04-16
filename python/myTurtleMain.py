from python.myTurtle import  *
import turtle

## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, txtSize = [0] * 4

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(10)

inStr = getString() #('문자열 입력', '거북이 쓸 문자열을 입력')
for ch in inStr :
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight) 
    r, g, b = getRGB() 
    turtle.goto(tX, tY)
    turtle.left(tAngle)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font = ('맑은고딕', txtSize, 'bold'))
turtle.done()