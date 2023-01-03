# 백준 25707번 팔찌 만들기
import sys
put = sys.stdin.readline

N = int(put())
n = sorted([int(_) for _ in put().split()])
n[-2], n[-1] = n[-1], n[-2]
answer = n[-1] - n[0]

for i in range(N-1):
    answer += abs(n[i+1] - n[i])

print(answer)