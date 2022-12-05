# 백준 17262번 팬덤이 넘쳐흘러
import sys
put = sys.stdin.readline

N = int(put())
s, e = 100000, 0

while N:
    N -= 1
    si, ei = map(int, put().split())

    s = min(s, ei)
    e = max(e, si)

if s < e:
    print(e - s)
else:
    print(0)