# 백준 26546번 Reverse
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    text, i, j = put().split()
    i, j = int(i), int(j)

    print(text[:i] + text[j:])