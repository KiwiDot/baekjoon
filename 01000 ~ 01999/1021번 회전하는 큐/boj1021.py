# 백준 1021번 회전하는 큐
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
queue = [i for i in range(1, N+1)]
loc = [int(_) for _ in put().split()]
cnt = 0

for i in loc:
    idx = queue.index(i)
    cnt += min(idx, len(queue) - idx)
    queue = queue[idx+1:] + queue[:idx]

print(cnt)
