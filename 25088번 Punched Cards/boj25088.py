# 백준 25088번 Punched Cards
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    R, C = map(int, put().split())

    print("Case #{}:".format(t))
    print(".." + '-'.join(['+'] * C))
    print(".." + '.'.join(['|'] * C))
    print("-".join(['+'] * (C + 1)))

    for i in range(R-1):
        print(".".join(['|'] * (C + 1)))
        print("-".join(['+'] * (C + 1)))