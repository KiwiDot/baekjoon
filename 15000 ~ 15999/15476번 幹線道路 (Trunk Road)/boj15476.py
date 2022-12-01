# 백준 15476번 幹線道路 (Trunk Road)
import sys
put = sys.stdin.readline

H, W = map(int, put().split())
A = [[int(_) for _ in put().split()] for i in range(H)]
cnt = []

for h in range(H):
    for w in range(W):
        a = 0
        for i in range(H):
            for j in range(W):
                a += min(abs(h-i), abs(w-j)) * A[i][j]

        cnt.append(a)

print(min(cnt))