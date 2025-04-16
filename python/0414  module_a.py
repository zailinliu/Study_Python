import python.module as module # module파일안에 있는 모든 함수를 가져오기
from python.module2 import func3 #module2파일안에 있는 함수중 필요한 함수만 가져오기
import sys
import math
import time
import datetime 
from datetime import datetime as dt
import random
from tkinter.simpledialog import *

module.func1()
module.func2()
module.func3()

func3()

print(sys.builtin_module_names)

print(math.log(10))

list_1 = [10,50,77,90]
print(math.fsum(list_1))

# 거듭제곱
a = 3
print(math.pow( a, 3))

print(math.pi)

# UTC 표준 시를 기준으로 한 현재시간 구함, 타임 스탬프 시간 
# 1970년 1월 1일 0시 0분 부터 현재까지의 초 값을 실수로 표기
utc = time.time() 
gm = time.gmtime(utc)
print(gm)
tm = time.localtime(time.time())
print('현재년도 : ' ,tm.tm_year)
print('현재 월 : ' ,tm.tm_mon)
print('현재 일 : ' ,tm.tm_mday)
print('현재 시 : ' ,tm.tm_hour)
print('현재 분 : ' ,tm.tm_min)
print('현재 초 : ' ,tm.tm_sec)

string = time.ctime(time.time())
print(string)

tm = time.localtime(time.time())
string = time.strftime('%Y-%m-%d %I:%M:%S %p',tm)

today = datetime.date.today()
print(today)

now = dt.now()
print(now)
today = dt.today()
print(today)
