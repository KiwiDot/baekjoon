# 백준 15887번 욱제는 결벽증이야!!
import sys
put = sys.stdin.readline

N = int(put())
card = [int(i) for i in put().split()]
op = 0
LR = []

for L in range(N):
    for R in range(L, N):
        if card[L] > card[R]:
            op += 1
            LR += [[str(L+1), str(R+1)]]
            card = card[:L] + card[L:R+1][::-1] + card[R+1:]

print(op)
for i in LR:
    print(' '.join(i))