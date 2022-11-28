# 백준 26068번 치킨댄스를 추는 곰곰이를 본 임스 2
import sys
put = sys.stdin.readline

N = int(put())
cnt = 0

while N:
    N -= 1
    x = int(put().strip()[2:])

    if x <= 90:
        cnt += 1

print(cnt)