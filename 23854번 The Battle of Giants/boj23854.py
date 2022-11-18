# 백준 23854번 The Battle of Giants
import sys
put = sys.stdin.readline

a = int(put())
b = int(put())

vic_a = a // 3
vic_b = b // 3

if a % 3 == b % 3:
    print(vic_a, a % 3, vic_b)

else:
    print(-1)