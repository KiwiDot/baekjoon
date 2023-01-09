# 백준 10157번 자리배정
import sys
put = sys.stdin.readline

C, R = map(int, put().split())
K = int(put())
K = 0 if K > C * R else K
x, y = [1], [0]
move = {'U': R, 'R': C-1, 'D': R-1, 'L': C-2}
drt = {'U': ['R', y, 1], 'R': ['D', x, 1], 'D': ['L', y, -1], 'L': ['U', x, -1]}
d = 'U'

while K:
    if K > move[d]:
        K -= move[d]
        drt[d][1][0] += move[d] * drt[d][2]
        move[d] -= 2
        d = drt[d][0]
    else:
        drt[d][1][0] += K * drt[d][2]
        K = 0

print(x[0] if y[0] else 0, y[0] if y[0] else '')

