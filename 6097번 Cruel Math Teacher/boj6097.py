# 백준 6097번 Cruel Math Teacher
import sys
put = sys.stdin.readline

N, P = map(int, put().split())
answer = str(N ** P)

for i in range(0, len(answer), 70):
    print(answer[i:i+70])