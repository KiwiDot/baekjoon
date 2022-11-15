# 백준 4841번 Look and Say
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    num = put().strip()
    cnt = 0
    n = []

    for i in num:
        if not n:
            n.append(i)
            cnt += 1

        elif n[-1] == i:
            cnt += 1

        else:
            n.insert(len(n)-1, str(cnt))
            n.append(i)
            cnt = 1

    n.insert(len(n)-1, str(cnt))
    print(''.join(n))