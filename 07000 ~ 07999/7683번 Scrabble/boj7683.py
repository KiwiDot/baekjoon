# 백준 7683번 Scrabble
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break

    word = [list(put().strip()) for i in range(n)]
    tile = [0] * 27
    for i in put().strip():
        if i == '_':
            tile[-1] += 1
        else:
            tile[ord(i)-65] += 1

    cnt = 0

    for i in word:
        w = 0
        for j in list(set(i)):
            c = i.count(j)
            if c > tile[ord(j)-65]:
                w += c - tile[ord(j)-65]

        if w <= tile[-1]:
            cnt += 1

    print(cnt)