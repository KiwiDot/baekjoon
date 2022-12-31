# 백준 c
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    word = put().strip()
    k = len(word)

    print(word)
    for i in range(1, k-1):
        print(word[i] + ' ' * (k-2) + word[k-i-1])
    if k > 1:
        print(word[::-1])