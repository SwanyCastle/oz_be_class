# 경로와 확장자 이용해 파일 찾고, 내용읽기

import os

def searchFile(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        # 내가 방금 만든게 디렉터리 인가를 확인
        # 하위 디렉터리가 있을 수도 있기에 하위 디렉터리도 확인하기위해
        # 재귀적으로 그 디렉터리 안에 내용도 확인해 볼 필요가 있다.
        if os.path.isdir(filepath):
            searchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, "r", encoding="utf-8") as f:
                    print(f.read())

searchFile("/Users/kwakseunghwan/OZ/oz_be_class", ".js")
searchFile("/Users/kwakseunghwan/OZ/oz_be_class", ".txt")