# 백준 26005번 나뭇잎 학회
import sys
put = sys.stdin.readline

N = int(put())

if N == 1:
    print(0)
else:
    print(N ** 2 // 2 + 1 if N ** 2 % 2 else N ** 2 // 2)