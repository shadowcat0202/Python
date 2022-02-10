print("나는 '대한민국' 이라고 말했다")  #큰따옴표 안에 작은 따옴표는 하나의 문자열로 취급
print("I don\'t know")  #\(역슬레쉬)는 특수한 성질을 지우고 문자열로 바꿔버린다

#문자열에 변수의 값을 삽입하여 출력하고 싶으면 %s를 이용한다
price = 1000
print("상품의 가격은 %s원 입니다." %price)

message = "현재 시간은 %s입니다"
time = "12:00pm"
print(message %time)    #%위치에 time이라는 변수를 넣는다

message = "오늘은 %s월 %s일입니다."
print(message %(3,1))   #2개도 가능하다

