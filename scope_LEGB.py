# python scope rule
# Local > Enclosed > Global > Built-in

# Local : 가장 가까운 함수안 범위
# Enclosed : 파이썬은 함수 안에 함수가 정의 될 수 있는 데, 가장 가까운 함수가 아닌 두번째 이상의 함수 가까운 함수범위
# Global : 함수 바깥의 변수 또는 import 된 module
# Built-in : 파이썬 안에 내장 함수, 속성

a = 5
b = 10


def outer():
    a = 10

    def inner():
        c = 30
        print(a, b, c)

    inner()
    a = 22
    inner()


outer()

# 똑같은 변수가 local과 global에 선언되었을 경우, LEGB rule에 따라 local 우선 사용
i = 1


def foo():
    i = 5
    print(i, " in foo() ")


print(i, " in global ")
foo()