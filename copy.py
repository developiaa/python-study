import copy

a = [1, 2, 3]
b = a
# shallow copy - 메모리 주소값이 복사되어 같은 값이 출력됨
print(id(a))
print(id(b))

c = [[1, 2, 3], [4, 5, 6]]
d = c[:]

# 슬라이싱을 통해 할당하는 경우 새로운 id가 부여되며, 서로 영향을 받지 않음
# 그러나 이러한 슬라이싱 또한 얕은 복사에 해당
# mutable 객체 안에 mutable 객체인 경우 문제가 된다.
# id(c) , id(d) 값은 다르지만 내부의 객체 id(c[0]), id(d[0])은 같다
print(id(c))
print(id(d))
print()
print(id(c[0]))
print(id(d[0]))

# c[0]= [1]과 같이 재할당하는 경우에는 메모리 주소가 변경된다.
c[0] = [99]
# 다른 값 출력
print(c)
print(d)
print()

# 하지만 c[0]에 값을 변경하는 경우에는 d[0]에 값도 변경된다.
c = [[1, 2, 3], [4, 5, 6]]
d = c[:]
c[1].append(4)
# 동일한 값 출력
print(c)
print(d)

# 깊은 복사를 하는 경우 내부 객체들까지 새롭게 할당된다.


e = [[1, 2], [3, 4]]
t = copy.deepcopy(e)

e[0].append(9)
print(e)
print(t)
