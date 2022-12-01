# 백준 9625번 BABBA
import sys
put = sys.stdin.readline

K = int(put())
a, b = 1, 0

while K:
    K -= 1
    a, b = b, a + b

print(a, b)