# 백준 25371번 k진수 정수의 자릿수 나누기
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
a = ""

# a는 n을 k진수로 변환한 수
while n:
    n, n_ = divmod(n, k)
    a += str(n_)

a = a[::-1]

# b는 a의 각 자릿수를 0을 기준으로 나눈 집합
b = [int(_) for _ in a.split('0') if _]

# 집합 b에 있는 수의 합을 k진수로 출력
b = sum(b)
answer = ""

while b:
    b, b_ = divmod(b, k)
    answer += str(b_)

print(answer[::-1])
