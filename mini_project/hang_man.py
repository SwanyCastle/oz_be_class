# Quiz) 행맨 게임(영어 단어 퀴즈) 프로그램

#     - 리스트에 3개 이상의 단어를 추가
#       예) apple, banana, orange

#     - 위 리스트에서 랜덤으로 1개의 단어를 선택

#     - 단어의 길이에 맞게 밑줄 출력
#       예) apple 의 경우 _____(밑줄 5개)

#     - 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct'출력, 아니면 'Worng'출력

#     - 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 밑줄 출력)
#       예) a 입력 시 : a____
#           p 입력 시 : app__
#           c 입력 시 : app__

#     - 정답을 맞히면 'Success' 출력 후 프로그램 종료(단, 횟수 제한 없음)

# 랜덤 함수 사용을 위해 import
from random import *
import re

# 에러캐치를 위한 클래스 생성
# 지정한 글지수 벗어나면 발생하는 에러
class NumberOfCharacter(Exception):
    def __init__(self):
        pass
# 숫자가 입력되면 발생하는 에러
class InputedNumber(Exception):
    def __init__(self):
        pass

# 한글이 입력되면 발생하는 에러
class InputedKorean(Exception):
    def __init__(self):
        pass    

# 한글 입력 확인
def is_korean(text):
    # 한글표현 정규식 = '[ㄱ-ㅎ가-힣]+'
    korean_pattern = re.compile('[ㄱ-ㅎ가-힣]+')
    return bool(korean_pattern.match(text))

# 초기 단어 셋팅
class Words:
    def __init__(self, word1, word2, word3) -> None:
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
    
    def select_word(self):
        word_list = [self.word1, self.word2, self.word3]
        index = randint(0,2)
        return word_list[index]

# 선택된 단어 자릿수에 맞는 "_" 출력 함수
def create_underbar(word):
    word_num = len(word)
    underbar = "_" * word_num
    return underbar

# 사용자가 입력한 글자가 선택된 단어(정답)에 포함되는지 체크후 리스트에 저장
def judge_word(user_input, correct_word, input_word_list):
    if user_input in correct_word:
        input_word_list.append(user_input)
        print("Correct. '{0}'는 단어에 포함된 글자입니다.\n".format(user_input))
    else:
        print("Worng. '{0}'는 단어에 포함된 글자가 아닙니다.\n".format(user_input))
    return input_word_list

# 선택된 단어(정답)을 맞춰가는 과정을 출력 맞춘 곳은 알파벳을 표현해주고 못맞힌곳은 "_"로 표현
def print_word(rand_word, input_word_list):
    element_list = []
    for i in rand_word:
        if i in input_word_list:
            element_list.append(i)
        else:
            element_list.append("_")
    print("문제) '{0}'\n".format("".join(element_list)))
    return element_list

# 초기 단어 생성
user = Words("coffee", "banana", "cake")

# 랜덤으로 단어 선택
rand_word = user.select_word()

# 선택된 단어(정답)의 글자수에 맞는 "_"출력
underbar_word = create_underbar(rand_word)

input_word_list = []

# 메인 처리
while True:
    try:
        user_input = input("'{0}'에 들어갈 알파벳 하나를 입력하세요. > ".format(underbar_word))
        if len(user_input) > 1:
            raise NumberOfCharacter
        elif user_input.isdigit():
            raise InputedNumber
        elif is_korean(user_input):
            raise InputedKorean
        else:
            input_word_list = judge_word(user_input, rand_word, input_word_list)
            result_word_list = print_word(rand_word, input_word_list)

            if "_" in result_word_list:
                a = len(result_word_list)
                b = len(rand_word)
                continue
            elif "".join(result_word_list) == rand_word:
                print("Success, 단어를 완성했습니다.")
                break
    except NumberOfCharacter:
        print("잘못 입력하셨습니다. '{0}' <한 글자만 입력해 주세요.>\n".format(user_input))
    except InputedNumber:
        print("잘못 입력하셨습니다. '{0}' <글자를 입력해 주세요.>\n".format(user_input))
    except InputedKorean:
        print("잘못 입력하셨습니다. '{0}' <영어를 입력해 주세요.>\n".format(user_input))


