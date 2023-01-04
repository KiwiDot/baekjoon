# 백준 23028번 5학년은 다니기 싫어요
import sys
put = sys.stdin.readline

N, A, B = map(int, put().split())
n = 8 - N  # 남은 학기 수

for i in range(10):
    X, Y = map(int, put().split())
    if i < n:
        x = X
        y = min(Y, 6 - x)
        A += x * 3
        B += (x + y) * 3

if A >= 66 and B >= 130:
    print("Nice")
else:
    print("Nae ga wae")