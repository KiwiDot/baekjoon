# 백준 4117번 Combination Lock
import sys
put = sys.stdin.readline

while True:
    N, T1, T2, T3 = map(int, put().split())
    if N == T1 == T2 == T3 == 0:
        break

    # 다이얼의 첫 위치가 T1과 최악인 경우
    cnt = 3 * N - 1

    # T1과 T2 사이의 눈금 수
    cnt += (T2 - T1 + N) % N + N

    # T2와 T3 사이의 눈금 수
    cnt += (T2 - T3 + N) % N

    print(cnt)