# 백준 12572번 Rope Intranet (Large)
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    N = int(put()) - 1
    rope = [[int(_) for _ in put().split()]]
    cnt = 0

    while N:
        N -= 1
        r = [int(_) for _ in put().split()]
        for i in rope:
            if (i[0] < r[0] and i[1] > r[1]) or (i[0] > r[0] and i[1] < r[1]):
                cnt += 1

        rope.append(r)

    print("Case #{}: {}".format(t, cnt))