# 백준 16408번 Poker Hand
import sys
put = sys.stdin.readline

rank = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0}
card = put().split()

for i in card:
    rank[i[0]] += 1

print(max(rank.values()))