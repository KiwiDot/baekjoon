# 백준 24937번 SciComLove (2022)
import sys
put = sys.stdin.readline

N = int(put())
s = "SciComLove"
N %= len(s)

print(s[N:] + s[:N])