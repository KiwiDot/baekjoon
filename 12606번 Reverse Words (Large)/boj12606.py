# 백준 12606번 Reverse Words (Large)
import sys
put = sys.stdin.readline

N = int(put())

for i in range(1, N+1):
    L = put().split()[::-1]

    print("Case #{}: {}".format(i, ' '.join(L)))