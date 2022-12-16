# 백준 25757번 임스와 함께하는 미니게임
import sys
put = sys.stdin.readline

N, game = put().split()
N = int(N)
g = {'Y': 1, 'F': 2, 'O': 3}[game]
n = set([put().strip() for i in range(N)])

print(len(n) // g)