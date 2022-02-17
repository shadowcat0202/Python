def test_name(name):
    print("test(" + name + ")")

def test_name_int(name, num):
    print("test(" + name + ", " + str(num) + ")")

def test_squared_num(num):
    '''
    :param num: 제곱 피연산
    :return:    제곱값
    '''
    print("test_squared_num(" + str(num) + ")")
    return num ** 2

def get_max(num1, num2):
    '''
    :param num1:(int)비교수1
    :param num2:(int)비교수2
    :return:    (int)큰값
    
    #파이썬에서는 대부분의 언어에서의 삼항연산자 [condition] ? [true_value] : [false_value]를 지원하지 않는다
    #[ture_value] if [condition] else [false_value] 형태이다
    '''
    return num1 if(num1 > num2) else num2
