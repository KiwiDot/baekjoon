# 백준 15449번 Art
import sys
put = sys.stdin.readline

l = sorted([int(_) for _ in put().split()])
cnt = 0

for a in range(3):
    for b in range(a+1, 4):
        for c in range(b+1, 5):
            if l[a] + l[b] > l[c]:
                cnt += 1

print(cnt)