# 백준 11922번 BELA
import sys
put = sys.stdin.readline

N, B = put().split()
card = {'A': [11, 11], 'K': [4, 4], 'Q': [3, 3], 'J': [20, 2],
        'T': [10, 10], '9': [14, 0], '8': [0, 0], '7': [0, 0]}
cnt = 0

for i in range(int(N) * 4):
    c = put().strip()
    if c[1] == B:
        cnt += card[c[0]][0]
    else:
        cnt += card[c[0]][1]

print(cnt)