# 백준 25375번 아주 간단한 문제
import sys
put = sys.stdin.readline

Q = int(put())

while Q:
    Q -= 1
    a, b = map(int, put().split())

    # a는 b의 약수, x y는 자연수
    if not b % a and b // a > 1:
        print(1)
    else:
        print(0)