# os 파일 시스템 관련 함수
import os

pwd = "/Users/kwakseunghwan/OZ/oz_be_class"

filenames = os.listdir()
print(filenames)

# 디렉터리인지 아닌지 여부
print(os.path.isdir(filenames[0]))
print(os.path.isdir(filenames[4]))
print(os.path.isdir(pwd + "/OS_chapter"))

# 파일인지 아닌지 여부
print(os.path.isfile(filenames[0]))
print(os.path.isfile(filenames[4]))
print(os.path.isfile(pwd + "/OS_chapter"))

# 파일 이름과 확장자 분리
filepath = pwd + "/" + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)