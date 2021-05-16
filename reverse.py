s = [10, 1, 7, 3]
s.sort()
print(s)
print()
s = [10, 1, 7, 3]
s.sort(reverse=True)
print(s)
print()
# 딕셔너리 정렬
data = [{'name': 'AA', 'price': 32.2, 'shares': 100},
        {'name': 'IBM', 'price': 91.1, 'shares': 50},
        {'name': 'CAT', 'price': 83.44, 'shares': 150},
        {'name': 'MSFT', 'price': 51.23, 'shares': 200},
        {'name': 'GE', 'price': 40.37, 'shares': 95},
        {'name': 'MSFT', 'price': 65.1, 'shares': 50},
        {'name': 'IBM', 'price': 70.44, 'shares': 100}]


def stock_name(s):
    return s['name']


# key 값을 통해 정렬조건을 받을 수 있다.
data.sort(key=stock_name)
print(data)
print()
# 콜백함수
# 위의 예시는 콜백함수의 일종이다. key값이 직접 제공한 함수를 콜백한다.
# 위의 예시를 람다:익명함수로 변경
data2 = [{'name': 'AA', 'price': 32.2, 'shares': 100},
        {'name': 'IBM', 'price': 91.1, 'shares': 50},
        {'name': 'CAT', 'price': 83.44, 'shares': 150},
        {'name': 'MSFT', 'price': 51.23, 'shares': 200},
        {'name': 'GE', 'price': 40.37, 'shares': 95},
        {'name': 'MSFT', 'price': 65.1, 'shares': 50},
        {'name': 'IBM', 'price': 70.44, 'shares': 100}]

data2.sort(key=lambda s: s['name'])
print(data2)