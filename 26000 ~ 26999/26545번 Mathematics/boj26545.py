# 백준 26545번 Mathematics
import sys
put = sys.stdin.readline

n = int(put())
calculator = sum([int(put()) for i in range(n)])
print(calculator)