# 백준 15738번 뒤집기
import sys
put = sys.stdin.readline

N, K, M = map(int, put().split())
A = put().split()

while M:
    M -= 1
    i = int(put())

    # 배열 A의 처음 i개의 순서를 뒤집는다
    if i > 0:
        if K <= i:
            K = i - K + 1

    # 배열 A의 마지막 -i개의 순서를 뒤집는다.
    else:
        if K >= N + i + 1:
            K = 2 * N - K + i + 1

print(K)