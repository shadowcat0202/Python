#리스트
#valuable = [value1, value2, ...] #물론 String형은 'value1'와 같은 방법으로 입력
shopping_list = ['milk', 'eggs', 'cheese', 'butter', 'cream']
print(type(shopping_list), shopping_list)
shopping_list[2] = 'apple'  #항목 변경 가능
print(type(shopping_list), shopping_list, "->[2]번 리스트 변경")
list_length = len(shopping_list)
print(list_length)

name = input("이름:")
age = int(input("나이:"))
address = input("주소:")
tall = int(input("키:"))

person = [name, age, address, tall]
print(person)