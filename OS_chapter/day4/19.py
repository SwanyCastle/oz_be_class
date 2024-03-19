foods = ["햄버거", "샐러드", "비스킷"]

print(id(foods))
print(hex(id(foods)))

# b"" -> 바이트 단위로 저장한다는 접둣
mw = memoryview(b"happy day")

print(mw)
print(mw[0])
print(mw[1])
print(mw[2])
print(mw[3])