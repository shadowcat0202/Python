'''
함수의 사용 이유
1. 중복된 코드 제거
2. 복잡한 작업을 더 간단한 작업들로 분해할 수 있다
3. 재사용 증가
4. 가독성 증대, 유지관리 간단
===============================================
def function_name([parameter1, paremter2, ...]):    #선언부(헤더)
    body                                            #구현부(정의부, 몸체)
    [return return_value]
===============================================
'''

def say_hello(name):
    print("say_hello(" + name + ")")

#파이썬에서는 오버로딩의 개념이 없다 
#마지막에 선언된 함수로 처리된다
# def say_hello(name, mag):
#     print("안녕하세요, " + name)
say_hello("홍길동")

#from hello import *
#->hello 파일의 내용을 전부 다 가져오기 때문에 파일이름.함수명으로 접근할 필요 없음
import stub_function   #->파일명.함수명으로 접근 필요
stub_function.test_name("이순신")
stub_function.test_name_int("강감찬", 20)

print("\n============입력과 반환값이 있는 사용자 정의 함수===================")
num = 5
print(str(num) + "**2=" + str(stub_function.test_squared_num(num)))

print("\n=============큰 값 함수===================")
comp_num = [6, 5]
print(str(comp_num) + "중에 큰 값은:" + str(stub_function.get_max(comp_num[0], comp_num[1])))