# 백준 4500번 “Bubble Gum, Bubble Gum, in the dish, how many pieces do you wish?”
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    p = put().split()
    gum = put().strip()
    n = int(put())
    p *= n

    idx = p.index(gum)
    print(p[idx+n-1])