# 백준 12517번 Centauri Prime (Small1)
import sys
put = sys.stdin.readline

T = int(put())

for x in range(1, T+1):
    C = put().strip()

    if C[-1] == 'y':
        Y = "nobody"

    elif C[-1] in ['a', 'e', 'i', 'o', 'u']:
        Y = "a queen"

    else:
        Y = "a king"

    print("Case #{}: {} is ruled by {}.".format(x, C, Y))
