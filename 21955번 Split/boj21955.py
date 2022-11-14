# 백준 21955번 Split
import sys
put = sys.stdin.readline

N = put().strip()
n = len(N) // 2

print(N[:n], N[n:])