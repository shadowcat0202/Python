def string_basic():
    print("나는 '대한민국'이라고 말헀다")   #큰따옴표 안에 작은 따옴표는 하나의 문자열로 취급
    
    print("I don\'t know")  #\(역슬레쉬)는 특수한 성질을 지우고 문자열로 바꿔버린다
    print(r"c:\temp\name\a.mp3")    #문자열 앞에 r을 붙이면 \t, \n과 같은 이스케이프 문자들의 기능을 무시한다(중요!)

    #문자열에 변수의 값을 삽입하여 출력하고 싶으면 %s를 이용한다
    
    price = 1000
    print("상품의 가격은 %s원 입니다." %price)

    message1 = "현재 시간은 %s입니다"
    time = "12:00pm"
    print(message1 %time)    #%위치에 time이라는 변수를 넣는다

    message2 = "오늘은 %s월 %s일입니다."
    print(message2 %(3,1))   #2개도 가능하다

    message_length = len(message1)
    print(message_length)

    #문자열 연결은 타입이 일치 해야한다(String + String)
    full_message = message2 +" "+ message1 + str(100)
    print(full_message)

    sentence = """
    나는 사람이고,
    파이썬은 쉬워요.
    """
    print(sentence)

def slicing():
    jumin = "990120-1234567"
    if int(jumin[7]) % 2 == 1:
        print("남성입니다")
    else:
        print("여성입니다")

    #<class:String>[a:b]    ->a인덱스부터 b-1 인덱스 까지
    #<class:String>[:b]     ->0인덱스부터 b-1 인덱스 까지
    #<class:String>[a:]     ->a인덱스부터 len(<class:String>)-1 인덱스 까지
    #<class:String>[-b:]    ->맨 뒤에서 b번째 인덱스부터 끝까지   
    print(jumin[-7:])  

def string_processing_function():
    python = "Python is Amazing"
    _python = python

    print("[",python,"]")
    
    #<class:String>.lower()
    print("<class:string>.lower()=", _python.lower())
    _python = python
    
    #<class:String>.upper()
    print("<class:string>.upper()=", _python.upper())
    _python = python
    
    #<class:String>[index].isupper() -> True / False
    print("<class:string>[].isupper()=", _python[0].isupper())
    _python = python
    
    #len(<class:String>)
    print("len(<class:string>)=", len(_python))

    #<class:String>.replace(<class:String>, <class:String>)
    print("<class:String>.replace(<class:string>, <class:string>)=",_python.replace("Python", "Java"))
    _python = python

    #<class:string>.index(<class:string>)
    index = _python.index("n")
    print("<class:string>.index(<class:string>)=", index)
    #<class:string>.index(<class:string>, <class:int>)  -> <class:int> 인덱스부터 탐색
    index = _python.index("n", index+1)
    print("<class:string>.index(<class:string>, <class:int>)=", index)

    #<class:string>.find(<class:string>)    ->  있으면 0 이상의 수 없으면 -1
    print("<class:string>.find(<class:string>)=", _python.find("Java"))

    #<class:string>.count(<class:string>)   -> 해당 문자 개수
    print("<class:string>.count(<class:string>)=", _python.count("n"))

def string_format():
    #[1-1] %d %s %c
    print(r"%d %s %c 설명-----------------------")
    print("나는 %d살입니다" % 20)               #정수
    print("나는 %s을 좋아해요" % "파이썬")      #문자열
    print("python은 %c로 시작해요" % "p", end="\n\n")       #문자

    #[1-2]
    print("나는 %s살입니다" % 20)   #%s로 해도 가능은 하다
    print("나는 %s와 %s를 좋아해요" % ("개", "고양이"), end="\n\n") #2개 이상도 가능하다

    #[2-1] .format()
    print(".format() 설명--------------------------------")
    print("나는 {}살입니다".format(20))
    print("나는 {}와 {}를 좋아해요".format("개", "고양이"))
    print("나는 {0}와 {1}를 좋아해요".format("개", "고양이"))
    print("나는 {1}와 {0}를 좋아해요".format("개", "고양이"), end="\n\n")

    #[2-2]
    print("나는 {age}살이며, {animal}을 좋아해요".format(age = 20, animal = "개"))
    print("나는 {age}살이며, {animal}을 좋아해요".format(animal = "개", age = 20), end="\n\n")  #순서를 바꿔도 변수에 매칭되기 때문에 가능하다

    #[2-3] python v3.6 이상
    age = 20
    animal = "강아지"
    print(f"나는 {age} 살이며, {animal}을 좋아해요", end="\n\n")    #실제 저장된 변수를 가져다가 사용

def escape_letter():
    # "\" 는 특수한 기능을 하는 문자를 만드는 역할
    '''
    \n : 줄바꿈
    \b : 백스페이스(한 글자 삭제)
    \t : 탭
    \r : 커서를 맨 앞으로 이동
    \["|'] : 문장 내 "" 혹은 ''를 적기 위해 사용
    \\ : "\"를 출력하기 위해 사용
    '''
    print("글자를 적을건데\n개행하고\t탭을치고 한글자(1234) 삭\b제\n개행한번더\"꾹!\"끝난다는 의미로 역슬레쉬\\")

