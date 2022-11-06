# 백준 6318번 Box of Bricks
import sys
put = sys.stdin.readline
idx = 0

while True:
    idx += 1
    n = int(put())
    if not n:
        break

    h = [int(_) for _ in put().split()]
    k, avg = 0, sum(h) // n

    for i in h:
        if i < avg:
            k += avg - i

    print("Set #{}".format(idx))
    print("The minimum number of moves is {}.".format(k))
    print()