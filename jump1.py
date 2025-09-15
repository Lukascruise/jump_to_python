# 1.1 1부터 5까지의 숫자를 제곱한 리스트 만들기
# 리스트 컴프리헨션의 'i'에 해당하는 값에 연산식을 넣을 수 있는지 궁금해했던 부분입니다.
numbers = [i**2 for i in range(1, 6)]
# 결과: [1, 4, 9, 16, 25]

# 1.2 1부터 3까지의 숫자를 문자열로 변환한 리스트 만들기
# str() 함수처럼 어떤 종류의 함수든 리스트 컴프리헨션에 넣을 수 있는지 궁금해했던 부분입니다.
list_of_strings = [str(i) for i in range(1, 4)]
# 결과: ['1', '2', '3']

# 1.3 1부터 5까지의 숫자 중 짝수/홀수를 구분한 리스트 만들기
# 삼항 연산자를 리스트 컴프리헨션과 함께 사용하는 방법을 연습했습니다.
numbers_type = ['even' if i % 2 == 0 else 'odd' for i in range(5)]
# 결과: ['even', 'odd', 'even', 'odd', 'even']

# 1.4 1부터 12까지의 숫자 중 10보다 크면 '크다', 아니면 '작다'로 구분한 리스트
# 삼항 연산자의 기본 구조를 연습했습니다.
num_size = ['크다' if i > 10 else '작다' for i in range(12)]
# 결과: ['작다', '작다', ..., '작다', '크다']

# 1.5 짝수 리스트와 홀수 리스트를 만들어 합치는 예제
# 두 개의 리스트 컴프리헨션을 합쳐서 여러 값을 처리할 수 있는지 궁금해했던 부분입니다.
even = [i for i in range(1, 11) if i % 2 == 0]
odd = [num for num in range(1, 11) if num % 2 != 0]
even.extend(odd)
# 결과: [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

# 1.6 함수 안에서 리스트 컴프리헨션과 삼항 연산자를 사용한 예제
def get_numbers(numbers):
    # 함수에 리스트 컴프리헨션을 넣어도 되는지 궁금해했던 부분입니다.
    num_type = ['짝수' if i % 2 == 0 else '홀수' for i in numbers]
    return num_type

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_numbers(my_numbers)

# 2.1 매개변수와 반환값이 없는 함수
# 함수를 만드는 가장 기본적인 방법입니다.
def hello():
    print("안녕하세요!")

# 2.2 매개변수만 있는 함수
def say_hello(name):
    # f-string을 사용해 매개변수를 문자열에 포함했습니다.
    print(f"안녕하세요, {name}님!")

# 2.3 반환값이 있는 함수
def add(a, b):
    # return으로 결과값을 반환합니다.
    return a + b

# 2.4 함수 호출 및 결과값 사용 예제
# 함수가 반환한 값을 변수에 저장하고 사용하는 과정을 연습했습니다.
result = add(3, 5)
print(result) # 결과: 8

# 2.5 함수 안에서 리스트 컴프리헨션을 사용한 예제
# 함수와 리스트 컴프리헨션이 어떻게 함께 사용되는지 보여줍니다.
def get_even_numbers(numbers):
    even_list = [num for num in numbers if num % 2 == 0]
    return even_list

my_list = [1, 2, 3, 4, 5, 6]
even_numbers = get_even_numbers(my_list)

# 3.1 __init__ 메서드를 사용한 클래스 예제
# 함수와 클래스, 메서드의 차이를 궁금해했던 부분을 다룹니다.
# self의 역할과 __init__의 의미를 배웠습니다.
class Person:
    def __init__(self, name, age):
        # self는 '나 자신'인 객체를 가리키며,
        # 객체의 속성(name, age)을 초기화하는 데 사용됩니다.
        self.name = name
        self.age = age

# 3.2 Person 클래스로 'lukas'라는 이름의 객체 만들기
# my_self는 클래스로 만든 객체 자신을 가리킵니다.
my_self = Person("lukas", 20)