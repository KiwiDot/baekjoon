# 백준 20651번 Daisy Chains
import sys
put = sys.stdin.readline

N = int(put())
p = [int(i) for i in put().split()]
cnt = 0

for i in range(N):
    for j in range(1, N-i+1):
        photo = p[i:i+j]
        if sum(photo) / j in photo:
            cnt += 1

print(cnt)