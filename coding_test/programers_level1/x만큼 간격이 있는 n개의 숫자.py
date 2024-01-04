# 내가 푼 거
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer

# 다른 사람이 푼것중에 맘에 드는거
def number_generator(x, n):
    # 함수를 완성하세요
    return [x*(i+1) for i in range(n)]