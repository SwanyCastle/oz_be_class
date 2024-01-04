# 내가 푼 문제
def solution(n):
    answer = 0

    str_list = list(str(n))

    for i in str_list:
        answer += int(i)

    return answer

# 다른 사람이 푼 문제 : 굳이 재귀함수로 풀어야하나? 반복문이 재귀함수보다 더 빠르다던데...
def sum_digit(number):
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)