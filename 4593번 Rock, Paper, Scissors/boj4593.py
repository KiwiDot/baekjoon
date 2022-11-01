# 백준 4593번 Rock, Paper, Scissors
import sys
put = sys.stdin.readline

p = {'R': 0, 'S': 1, 'P': 2}

while True:
    p1 = put().strip()
    p2 = put().strip()
    if p1 == p2 == 'E':
        break

    cnt1, cnt2 = 0, 0
    for i in range(len(p1)):
        r1, r2 = p[p1[i]], p[p2[i]]
        result = r1 - r2
        if result == 2 or result == -1:
            cnt1 += 1

        elif result == 1 or result == -2:
            cnt2 += 1

    print("P1: {}".format(cnt1))
    print("P2: {}".format(cnt2))

