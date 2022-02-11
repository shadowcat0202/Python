print("나는 '대한민국' 이라고 말했다")  #큰따옴표 안에 작은 따옴표는 하나의 문자열로 취급
print("I don\'t know")  #\(역슬레쉬)는 특수한 성질을 지우고 문자열로 바꿔버린다
print(r"c:\temp\name\a.mp3")    #\t, \n과 같은 이스케이프 문자들의 기능을 제거하기 위해서 문자열 앞에 r을 붙여준다(중요!)
#문자열에 변수의 값을 삽입하여 출력하고 싶으면 %s를 이용한다
price = 1000
print("상품의 가격은 %s원 입니다." %price)

message1 = "현재 시간은 %s입니다"
time = "12:00pm"
print(message1 %time)    #%위치에 time이라는 변수를 넣는다

message2 = "오늘은 %s월 %s일입니다."
print(message2 %(3,1))   #2개도 가능하다

message_length = len(message1);
print(message_length)

#문자열 연결은 타입이 일치 해야한다(String + String)
full_message = message2 +" "+ message1 + str(100)

print(full_message)