# 백준 13608번 Jogo de Varetas
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if not N:
        break
    cnt = 0

    while N:
        N -= 1
        C, V = map(int, put().split())
        cnt += V // 2

    print(cnt // 2)