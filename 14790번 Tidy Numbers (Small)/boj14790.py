# 백준 14790번 Tidy Numbers (Small)
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    N = put().strip()
    if len(N) == 1 or list(N) == sorted(list(N)):
        n = N

    else:
        for i in range(len(N)-1, -1, -1):
            n = N[:i-1] + str(int(N[i-1]) - 1) + '9' * (len(N) - i)
            if list(n) == sorted(list(n)):
                break

    print("Case #{}: {}".format(t, int(n)))