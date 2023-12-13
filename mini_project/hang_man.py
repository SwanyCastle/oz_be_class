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

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---""",
]

# 초기 단어 셋팅
class Words:
    def __init__(self, word1, word2, word3, word4, word5) -> None:
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
        self.word4 = word4
        self.word5 = word5
    
    def select_word(self):
        word_list = [self.word1, self.word2, self.word3, self.word4, self.word5]
        index = randrange(0,len(word_list))
        return word_list[index]
    
class HangmanGame:
    def __init__(self) -> None:
        # 초기 단어 생성
        user = Words("apple", "banana", "orange", "grape", "lemon")
        # 랜덤으로 단어 선택
        self.rand_word = user.select_word()

        self.input_word_list = []
        self.total_attempt = 6

    # 선택된 단어 자릿수에 맞는 "_" 출력 함수
    def create_underbar(self, word):
        word_num = len(word)
        underbar = "_" * word_num
        return underbar

    # 사용자가 입력한 글자가 선택된 단어(정답)에 포함되는지 체크후 리스트에 저장
    def judge_word(self, user_input, correct_word, input_word_list):
        if user_input in input_word_list:
            print("이미 추측한 글자 입니다. 다른 글자를 입력해 주세요.")
        else:
            if user_input in correct_word:
                input_word_list.append(user_input)
                print(hangman_pics[6 - self.total_attempt])
                print("단어를 맞추셨군요. 더 힘내봐요. '{0}'는 단어에 포함된 글자입니다.\n".format(user_input))
            else:
                self.total_attempt -= 1
                print(hangman_pics[6 - self.total_attempt])
                print("틀렸습니다. '{0}'는 단어에 포함된 글자가 아닙니다. <남은 시도 횟수 : {1}>\n".format(user_input, self.total_attempt) )
        return input_word_list

    # 선택된 단어(정답)을 맞춰가는 과정을 출력 맞춘 곳은 알파벳을 표현해주고 못맞힌곳은 "_"로 표현
    def print_word(self, rand_word, input_word_list):
        element_list = []
        for i in rand_word:
            if i in input_word_list:
                element_list.append(i)
            else:
                element_list.append("_")
        print("문제) '{0}'\n".format("".join(element_list)))
        return element_list

    def play(self):

        # 선택된 단어(정답)의 글자수에 맞는 "_"출력
        underbar_word = self.create_underbar(self.rand_word)

        # 메인 처리
        while self.total_attempt > 0:
            try:
                user_input = input("'{0}'에 들어갈 알파벳 하나를 입력하세요. > ".format(underbar_word))
                if len(user_input) > 1:
                    raise NumberOfCharacter
                elif user_input.isdigit():
                    raise InputedNumber
                elif is_korean(user_input):
                    raise InputedKorean
                else:
                    self.input_word_list = self.judge_word(user_input, self.rand_word, self.input_word_list)
                    result_word_list = self.print_word(self.rand_word, self.input_word_list)

                    if "_" in result_word_list:
                        continue
                    elif "".join(result_word_list) == self.rand_word:
                        print("축하합니다! 단어를 맞추셨습니다: {0}".format(self.rand_word))
                        break
            except NumberOfCharacter:
                print("잘못 입력하셨습니다. '{0}' <한 글자만 입력해 주세요.>\n".format(user_input))
            except InputedNumber:
                print("잘못 입력하셨습니다. '{0}' <글자를 입력해 주세요.>\n".format(user_input))
            except InputedKorean:
                print("잘못 입력하셨습니다. '{0}' <영어를 입력해 주세요.>\n".format(user_input))
        else:
            print(hangman_pics[-1])
            print("게임 오버. 정답은: {0}".format(self.rand_word))

if __name__ == "__main__":
    game = HangmanGame()
    game.play()