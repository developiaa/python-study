a: str = "1"
b: int = 1


# 타입 힌트 사용
# 다만 강제 규약이 아님
def fn(a: int) -> bool:
    if type(a) == int:
        return True
    return False


print(fn(a))
print(fn(b))
