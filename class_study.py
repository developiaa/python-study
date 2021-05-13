class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 인스턴스 메서드
    def calcArea(self):
        return self.width * self.height

    # 정적 메서드 - 인스턴스 데이터의 액세스할 필요가 없는 경우 클래스 메서드나 정적메서드를 사용
    @staticmethod
    def isSquare(rectWidth, recHeight):
        return rectWidth == recHeight

    # 클래스 메서드 - 클래스 변수를 액세스할 필요가 있을 때 사용
    @classmethod
    def printCount(cls):
        print(cls.count)

    # magic method or special method
    # __del__(소멸자), __sub__(두 개의 객체를 빼는), __cmp__(두 개의 객체 비교), __str__(문자열로 객체 표현) 등
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)


# 테스트
square = Rectangle.isSquare(5, 5)
print(square)

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()

r1 = Rectangle(10, 5)
r2 = Rectangle(20, 15)
r3 = r1 + r2  # __add__()가 호출됨
print(r3.width)
print(r3.height)

# 인스턴스 생성
r = Rectangle(2, 3)

# 메서드 호출
area = r.calcArea()
print("area : ", area)

# 인스턴스 변수 액세스
print("width before : ", r.width)
r.width = 10
print("width after : ", r.width)

# 클래스 변수 액세스
print(Rectangle.count)
print(r.count)
