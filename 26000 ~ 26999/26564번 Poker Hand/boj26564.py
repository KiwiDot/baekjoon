# 백준 26564번 Poker Hand
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    poker = {}

    for i in "A23456789TJQK"[::-1]:
        poker[i] = 0

    card = put().split()
    for i in range(5):
        poker[card[i][0]] += 1

    print(max(poker.values()))