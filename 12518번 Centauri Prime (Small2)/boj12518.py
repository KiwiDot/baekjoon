# 백준 12518번 Centauri Prime (Small2)
import sys
put = sys.stdin.readline

T = int(put())

for x in range(1, T+1):
    C = put().strip()

    if C[-1].lower() == 'y':
        Y = "nobody"

    elif C[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
        Y = "a queen"

    else:
        Y = "a king"

    print("Case #{}: {} is ruled by {}.".format(x, C, Y))