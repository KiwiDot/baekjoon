# 백준 16099번 Larger Sport Facility
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    lt, wt, le, we = map(int, put().split())
    area1 = lt * wt
    area2 = le * we

    if area1 > area2:
        print("TelecomParisTech")

    elif area1 < area2:
        print("Eurecom")

    else:
        print("Tie")