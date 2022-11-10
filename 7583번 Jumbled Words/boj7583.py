# 백준 7583번 Jumbled Words
import sys
put = sys.stdin.readline

while True:
    text = put().split()
    if text == ['#']:
        break

    for i in range(len(text)):
        t = list(text[i][::-1])
        t[0], t[-1] = t[-1], t[0]
        text[i] = ''.join(t)

    print(' '.join(text))