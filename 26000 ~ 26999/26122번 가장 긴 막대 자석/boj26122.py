# 백준 26122번 가장 긴 막대 자석
import sys
put = sys.stdin.readline

K = int(put())
magnet = put().strip()
m = 0
ncnt1 = ncnt2 = 0
scnt1 = scnt2 = 0

for i in magnet:
    if i == 'N':
        if not ncnt2:
            ncnt1 += 1

        else:
            m = max(m, min(ncnt1, ncnt2))
            ncnt1, ncnt2 = 1, 0

        if scnt1:
            scnt2 += 1

    else:
        if not scnt2:
            scnt1 += 1

        else:
            m = max(m, min(scnt1, scnt2))
            scnt1, scnt2 = 1, 0

        if ncnt1:
            ncnt2 += 1

m = max(m, min(ncnt1, ncnt2), min(scnt1, scnt2))
print(m * 2)