# 백준 26510번 V for Vendetta
import sys
put = sys.stdin.readline


def star(n):
    for i in range(n-1):
        print(' ' * i + '*' + ' ' * (2 * (n - i) - 3) + '*')
    print(' ' * (n-1) + '*')
    return 0


N = [int(_) for _ in put().split()]

for n in N:
    star(n)