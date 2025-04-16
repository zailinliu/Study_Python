# 문제1)
import math

radius = 5
area = math.pow(radius,2) * math.pi

print(area)

# 문제2)
import random

print(random.randint(1,100))

# 문제3)
import time

string = time.localtime(time.time())
st = time.strftime('%Y-%m-%d', string)
print(st)

import datetime

today = datetime.datetime.today()
stm = today.strftime('%Y-%m-%d')
print(stm)