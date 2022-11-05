# 백준 25993번 Medal Ranking
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    medal = [int(_) for _ in put().split()]
    USA = medal[:3]
    Russia = medal[3:]

    u = USA[0] * 1000000 + USA[1] * 1000 + USA[2]
    r = Russia[0] * 1000000 + Russia[1] * 1000 + Russia[2]
    count = False
    color = False

    if sum(USA) > sum(Russia):
        count = True
    if u > r:
        color = True

    print(' '.join([str(_) for _ in medal]))

    if count and color:
        print("both")

    elif count:
        print("count")

    elif color:
        print("color")

    else:
        print("none")

    print()