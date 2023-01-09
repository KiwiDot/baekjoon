# 백준 5568번 카드 놓기
import sys
import itertools
put = sys.stdin.readline

n = int(put())
k = int(put())
card = [put().strip() for i in range(n)]
num = set()

for i in itertools.permutations(card, k):
    num.add(''.join(list(i)))

print(len(num))