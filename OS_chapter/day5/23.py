# 기본적인 파일 입출력 예제

with open("number_one.txt", "w") as f:
    f.write("one!")
with open("number_tow.txt", "w") as f:
    f.write("two!")
with open("number_three.txt", "w") as f:
    f.write("three!")
with open("number_four.txt", "w") as f:
    f.write("four!")

# 여러개의 파일을 한꺼번에 처리하고 싶을 때 사용
# 파일 네임의 패턴을 이요해 한꺼번에 접근하기
import glob

for filename in glob.glob("*.txt", recursive=True):
    print(filename)

# glob 을 이용해서 한꺼번에 접근 하는과 동시에 그 내용들 까지도 같이 처리
import fileinput

with fileinput.input(glob.glob("*.txt")) as fi:
    for line in fi:
        print(line)

# 파일 이름에서 공통된 패턴이나 정규 표현식으로 찾을 때 사용
import fnmatch, os

for filename in os.listdir('.'):
    # if fnmatch.fnmatch(filename, "??????_one.txt"):
    # if fnmatch.fnmatch(filename, "??????_???.txt"):
    if fnmatch.fnmatch(filename, "??????_*.txt"):
        print(filename)


