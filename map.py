a = [1, 2, 3, 4, 5]

for i in range(len(a)):
    a[i] = int(a[i])
print(a)

# map()은 원본 데이터를 변경하지 않고 지정된 함수로 처리해주는 함수
# map(func, *iterables)
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
b = list(map(int, a))
print(b)
print(id(a))
print(id(b))

# map의 출력결과는 iterator이기 때문에 값을 확인할 수 없어 형변환을 통해 확인한다
k = [3, 4, 5, 6, 7]
p = map(lambda x: x + 1, k)
print(p)
print(list(p))