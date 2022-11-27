# 백준 16864번 So You Like Your Food Hot?
import sys
put = sys.stdin.readline

pt, p1, p2 = [int(round(float(_) * 100, 1)) for _ in put().split()]
cnt1 = -1
check = True

while True:
    cnt1 += 1
    cnt2 = -1

    while True:
        cnt2 += 1
        if p1 * cnt1 + p2 * cnt2 == pt:
            print(cnt1, cnt2)
            check = False
            break

        if p1 * cnt1 + p2 * cnt2 > pt:
            break

    if p1 * cnt1 > pt:
        break

if check:
    print("none")