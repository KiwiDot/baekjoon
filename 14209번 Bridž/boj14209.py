# 백준 14209번 Bridž
import sys
put = sys.stdin.readline

N = int(put())
card = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'X': 0}
c = ['A', 'K', 'Q', 'J', 'X'][::-1]
cnt = 0

while N:
    N -= 1
    s = put().strip()

    for i in s:
        card[i] += 1

for i in range(5):
    cnt += i * card[c[i]]

print(cnt)