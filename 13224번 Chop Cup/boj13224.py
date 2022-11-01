# 백준 13224번 Chop Cup
import sys
put = sys.stdin.readline

cup = [1, 0, 0]
ABC = put().strip()
chop = {'A': [0, 1], 'B': [1, 2], 'C': [0, 2]}

for i in ABC:
    i1, i2 = chop[i]
    cup[i1], cup[i2] = cup[i2], cup[i1]

print(cup.index(1) + 1)