# 백준 10187번 Golden
import sys
put = sys.stdin.readline

phi = 1.61803399
t = int(put())

while t:
    t -= 1
    f1, f2 = map(float, put().split())
    check = False

    if phi - 0.01 <= f1 / f2 <= phi + 0.01:
        check = True

    if phi - 0.01 <= f2 / f1 <= phi + 0.01:
        check = True

    print("golden" if check else "not")