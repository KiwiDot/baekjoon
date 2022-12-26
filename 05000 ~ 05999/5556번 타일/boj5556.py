# 백준 5556번 타일
import sys
put = sys.stdin.readline

N = int(put())
K = int(put())

while K:
    K -= 1
    a, b = map(int, put().split())
    color = min(min(a, N-a+1), min(b, N-b+1)) % 3
    if not color:
        color = 3

    print(color)