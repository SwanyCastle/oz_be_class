# 정수 n을 입력받아서 n의 약수들의 합을 구하는 문제

# 내가 푼 문제
# def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             answer += i
#     return answer

# # 다른사람이 푼 문제

# def solution(n):
#     # n이 만약 12 라면 12를 제외하고 6이상의 수로 나누어지지 않으니 
#     # 12를 반으로 쪼갠다음에 계산 하는 것이 큰수일 경우 반복문을 반만 실행하기에 성능이 향상됨
#     # 여기서 sum 함수는 순회가능하다면 사용 가능해서 for문을 사용한
#     return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
n = 12
print([i for i in range(1, (n // 2) + 1) if n % i == 0])