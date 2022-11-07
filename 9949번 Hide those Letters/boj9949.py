# 백준 9949번 Hide those Letters
import sys
put = sys.stdin.readline
idx = 0

while True:
    idx += 1
    w1, w2 = put().split()
    if w1 == w2 == '#':
        break

    n = int(put())

    print("Case {}".format(idx))
    while n:
        n -= 1
        word1 = put().strip()
        word2 = ""

        for i in word1:
            if i.lower() == w1 or i.lower() == w2:
                word2 += "_"
            else:
                word2 += i

        print(word2)
    print()