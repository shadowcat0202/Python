'''
반복문
[1]: for
===============================================
for variable in sequence:
    repeat
-----------------------------------------------
sequence(List or String):
range([start,] end [,step])
->default: start=0, step=1
start to end-1 each step
===============================================
[2]: while(통상, 무한루프용으로 많이 사용된다)
while conditional:
    repeat
-----------------------------------------------

===============================================
'''
'''
breakpoint(중단점)는 디버깅(에러를 잡아나가는 과정)에 아주 효율적으로 사용할 수가 있다.(단축키 Shift + F9)
한 과정씩 변수의 값이 변화되는 과정으로 살펴보기 위해서는 F7을 눌러가며 확인하여 디버깅을 할 수 있다.
'''

#정수 List를 시퀸스로 만드는 방법은 비효율적이다
for x in [0, 1, 2, 3, 4]:
    print(x, end=", ")

print("\n-----------------range(end)를 사용하는 방법---------------------")
print("range(5):", type(range(5)))
for x in range(5):
    print(x, end=", ")

print("\n-----------------String List sequence를 사용하는 방법---------------------")
s = ["가", "나", "다", "라", "마"]
for x in s:
    print(x, end=", ")

print("\n-----------------String을 사용하는 방법---------------------")
s = "This is String"
for ch in s:
    print(ch, end=" ")

print("\n-----------------range(start(3), end(10))---------------------")
for x in range(3, 10):
    print(x, end=", ")

print("\n-----------------range(start(1), end(10), step(2))---------------------")
for x in range(1, 10, 2):
    print(x, end=", ")

print("\n-----------------break를 사용하여 반복문을 빠져 나와보자---------------------")
hap = 0
for i in range(101):
    if hap >= 2000:
        print("마지막으로 더해진 i의 값:", i-1)
        break
    else:
        hap += i
print("hap:", hap)
'''
print("\n-----------------피보나치---------------------")
fi = int(input("피보나치 수열을 만들 정수(보다작을때까지)를 입력하세요:"))
fibo = [1, 1, 1]
for i in range(1, fi):
    if i < 3:
        fibo[2] = 1
    else:
        fibo[2] = fibo[1] + fibo[0]
        fibo[0] = fibo[1]
        fibo[1] = fibo[2]
    if fibo[2] < fi:
        print(fibo[2], end=" ")
'''
print("\n-----------------화씨-섭씨 변환---------------------")
#공식: C = (F - 32) * 5 / 9
for t in range(0, 101, 10):
    c = (t-32) * 5 / 9
    print(t, "->", round(c, 2))

import turtle
t = turtle.Pen()
'''
#별 그리기
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.exitonclick()
'''
'''
#사각형 회전하면서 그리기
square_num = 3
square_size = 50
between_square_angle = 20
for Square in range(square_num):
    for i in range(4):
        t.forward(square_size)
        t.right(90)
    t.left(between_square_angle)
turtle.exitonclick()

'''




