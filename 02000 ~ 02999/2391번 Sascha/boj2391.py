# 백준 2391번 Sascha
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    Sascha = put().strip()
    s = len(Sascha)
    w = int(put())
    dic = {}

    while w:
        w -= 1
        word = put().strip()
        cnt = 0

        for i in range(s):
            if word[i] != Sascha[i]:
                cnt += 1

        if cnt not in dic:
            dic[cnt] = word

    print(dic[min(dic.keys())])