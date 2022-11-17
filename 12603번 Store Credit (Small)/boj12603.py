# 백준 12603번 Store Credit (Small)
import sys
put = sys.stdin.readline

N = int(put())

for n in range(1, N+1):
    C = int(put())
    P = int(put())
    I = [int(_) for _ in put().split()]
    idx_i, idx_j = 0, 0

    for i in range(P-1):
        for j in range(i+1, P):
            if I[i] + I[j] == C:
                idx_i, idx_j = i + 1, j + 1
                break

        if idx_i and idx_j:
            break

    print("Case #{}: {} {}".format(n, idx_i, idx_j))