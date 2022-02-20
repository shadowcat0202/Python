def List_basic():
    #리스트
    #valuable = [value1, value2, ...] #물론 String형은 'value1'와 같은 방법으로 입력

    #숫자도 가능
    list = [10,20,30]
    print(type(list), list)
    #문자열도 가능
    list = ["홍길동", "바둑이", "영희"]
    print(type(list), list)
    #혼합도 가능
    list = [10, "홍길동" , '가']
    print(type(list), list)

    #<class:list>.index(variable)   -> return index
    print("\"홍길동\"의 위치(index)는 ",list.index("홍길동"))

    #<class:list>.append(variable)  -> list의 뒤에 추가
    list.append("append")
    print(list)

    #<class:list>.insert(index, variable)   ->list의 index위치에 variable을 삽입
    list.insert(1, "insert")
    print(list)

    #<class:list>.pop() -> 뒤에서 한개씩 꺼냄
    print("pop '",list.pop(),"'")
    print(list)

    #<class:list>.count(variable)  -> variable의 개수
    