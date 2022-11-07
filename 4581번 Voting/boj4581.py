# 백준 4581번 Voting
import sys
put = sys.stdin.readline

while True:
    s = put().strip()
    if s == '#':
        break

    cnt = {'Y': 0, 'N': 0, 'P': 0, 'A': 0}
    for i in s:
        cnt[i] += 1

    if cnt['A'] >= len(s) / 2:
        print("need quorum")

    elif cnt['Y'] > cnt['N']:
        print("yes")

    elif cnt['Y'] < cnt['N']:
        print("no")

    else:
        print("tie")