from random import *

'''
randint(a,b)    -> a~b사이의 정수를 랜덤으로 반환해주는 함수
random()        -> 0.0~1.0 미만의 임의의 값을 float 형태로 반환해주는 함수
randrange(start, stop, step) -> start부터 stop까지 step에 따라 반환
randrange(start) -> 0부터 start까지의 정수 반환
'''

print("1~6 중 하나:", randint(1,6))
print("0.0~1.0 사이의 float 수:", random())
print("randrange(0,101,2):", randrange(0,101,4))
print("randrange(10):", randrange(10))



