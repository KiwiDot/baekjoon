# 백준 16515번 Euler’s Number
import sys
import math
put = sys.stdin.readline

n = int(put())
e = 0

for i in range(n+1):
    e += 1 / math.factorial(i)

print(e)