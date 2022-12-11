# 백준 25631번 마트료시카 합치기
import sys
put = sys.stdin.readline

N = int(put())
a = [int(_) for _ in put().split()]
cnt = {}

for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

print(max(cnt.values()))