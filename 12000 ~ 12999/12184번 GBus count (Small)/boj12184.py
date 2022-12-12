# 백준 12184번 GBus count (Small)
import sys
put = sys.stdin.readline

T = int(put())

for x in range(1, T+1):
    N = int(put())
    GBus = [int(_) for _ in put().split()]
    A, B = [], []
    for i in range(0, N*2, 2):
        a, b = sorted([GBus[i], GBus[i+1]])
        A.append(a)
        B.append(b)

    y = []
    P = int(put())
    while P:
        P -= 1
        C = int(put())
        cnt = 0

        for i in range(N):
            if A[i] <= C <= B[i]:
                cnt += 1

        y.append(str(cnt))

    print("Case #{}: {}".format(x, ' '.join(y)))
    if x < T:
        blank = put()