# 백준 22016번 巻物 (Scroll)
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
T = put().strip()
S = T[:K-1] + T[K-1:].swapcase()

print(S)