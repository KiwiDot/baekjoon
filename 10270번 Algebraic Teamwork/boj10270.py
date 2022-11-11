# 백준 10270번 Algebraic Teamwork
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    answer = 1

    for i in range(1, n+1):
        answer = answer * i % 1000000007

    print(answer - 1)