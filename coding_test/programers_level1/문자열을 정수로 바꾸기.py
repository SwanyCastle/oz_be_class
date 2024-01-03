# 내 풀이
def solution(s): 
    return int(s)

# 다른사람이 푼 문제 - int()쓰지말라고 했으면 못풀었을 듯
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result
