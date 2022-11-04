# 백준 5679번 Hailstone Sequences
import sys
put = sys.stdin.readline

while True:
    H = int(put())
    if not H:
        break

    h = {H}
    while H != 1:
        if H % 2:
            H = 3 * H + 1
        else:
            H //= 2
        h.add(H)

    print(max(h))