# 백준 6889번 Smile with Similes
import sys
put = sys.stdin.readline

n = int(put())
m = int(put())

adjectives = [put().strip() for i in range(n)]
nouns = [put().strip() for i in range(m)]

for i in adjectives:
    for j in nouns:
        print(i, "as", j)