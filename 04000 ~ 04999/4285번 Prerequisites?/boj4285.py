# 백준 4285번 Prerequisites?
import sys
put = sys.stdin.readline

while True:
    data = [int(_) for _ in put().split()]
    if data == [0]:
        break

    k, m = data
    Freddie = set(put().split())
    check = True
    while m:
        m -= 1
        categories = put().split()
        r, c = categories[:2]

        if len(set(categories[2:]) & Freddie) < int(c):
            check = False

    if check:
        print("yes")
    else:
        print("no")