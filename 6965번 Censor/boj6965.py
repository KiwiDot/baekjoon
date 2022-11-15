# 백준 6965번 Censor
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    text = put().split()
    for i in range(len(text)):
        if len(text[i]) == 4:
            text[i] = "****"

    print(' '.join(text))
    print()