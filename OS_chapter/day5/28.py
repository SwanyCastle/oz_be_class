# 파일 복사 또는 이동
import os, shutil

pwd = "/Users/kwakseunghwan/OZ/oz_be_class"

filenaems = os.listdir(pwd)

for filename in filenaems:
    if "tokyo" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "copy.txt"))
        shutil.move(origin, os.path.join(pwd, "OS_chapter"))