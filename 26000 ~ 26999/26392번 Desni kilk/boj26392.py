# 백준 26392번 Desni kilk
import sys
put = sys.stdin.readline

n, r, s = map(int, put().split())

while n:
    n -= 1
    NFT = [put().strip() for i in range(r)]
    value = [r for i in range(s)]
    insecurity = []

    for i in range(r):
        for j in range(s):
            if NFT[i][j] == '#':
                insecurity.append(value[j])
            else:
                value[j] -= 1

    print(insecurity[0] - insecurity[-1])