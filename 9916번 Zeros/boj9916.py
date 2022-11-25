# 백준 9916번 Zeros
import sys
import math
put = sys.stdin.readline

N = int(put())
n = str(math.factorial(N))

print(n.count('0'))