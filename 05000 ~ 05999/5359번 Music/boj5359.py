# 백준 5359번 Music
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m, c = map(int, put().split())
    volume = [int(_) for _ in put().split()]
    cnt = 0

    for i in range(n-m+1):
        v = volume[i:i+m]
        if max(v) - min(v) <= c:
            cnt += 1

    print(cnt)
