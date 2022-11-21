# 백준 26004번 HI-ARC
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
cnt = {'H': 0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}

for i in S:
    if i in cnt:
        cnt[i] += 1

print(min(cnt.values()))