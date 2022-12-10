# 백준 18268번 Cow Gymnastics
import sys
put = sys.stdin.readline

K, N = map(int, put().split())
cow = set()

rank = put().split()
for i in range(N-1):
    for j in range(i+1, N):
        cow.add((rank[i], rank[j]))

for k in range(K-1):
    rank = put().split()
    for i in range(N-1):
        for j in range(i+1, N):
            if (rank[j], rank[i]) in cow:
                cow.discard((rank[j], rank[i]))

print(len(cow))
