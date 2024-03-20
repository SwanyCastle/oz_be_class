# 파일 관련 예외는 운영체제와 관계가 있다.

try:
    f = open("name.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print(e)
    # issubclass - 첫 번째 인자로 주어진 클래스가 두 번째 인자로 주어진 클래스의 하위클래스가 맞는지 확인 하는 함수
    print(issubclass(FileNotFoundError, OSError))
    print(issubclass(ZeroDivisionError, OSError))