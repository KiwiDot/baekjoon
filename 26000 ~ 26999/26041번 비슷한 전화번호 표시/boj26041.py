# 백준 26041번 비슷한 전화번호 표시
import sys
put = sys.stdin.readline

A = put().split()
B = put().strip()
cnt = 0

for i in A:
    if i != B and i.startswith(B):
        cnt += 1

print(cnt)