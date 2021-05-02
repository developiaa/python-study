#-*- coding: utf-8 -*-
def abc():
    if True:
        a = 5
    print(a)


abc()
# >>> 5

# print(a)
# >>> NameError: name 'a' is not defined

# 파이썬 스코프는 javascript의 var와 유사하다
# 같은 함수 안에 있고 if 바깥에서는 접근가능하나, 함수 밖에서는 불가능하다.


def test():
    a = [1, 3, 5]
    for i in a:
        print("i : ", i)
    print(i)


test()
