# 백준 18265번 MooBuzz
import sys
put = sys.stdin.readline

N = int(put())
n = N
cnt = N - (N // 3 + N // 5 - N // 15)

while N != cnt:
    n += 1
    if n % 3 and n % 5:
        cnt += 1

print(n)