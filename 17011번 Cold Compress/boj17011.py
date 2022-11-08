# 백준 17011번 Cold Compress
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    s = put().strip()
    compress = []
    cnt = 0

    for i in s:
        if not compress:
            compress.append(i)
            cnt += 1

        elif compress[-1] == i:
            cnt += 1

        else:
            compress.insert(len(compress)-1, str(cnt))
            compress.append(i)
            cnt = 1
    compress.insert(len(compress) - 1, str(cnt))

    print(' '.join(compress))