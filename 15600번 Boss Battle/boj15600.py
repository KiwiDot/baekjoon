# 백준 15600번 Boss Battle
import sys
put = sys.stdin.readline

n = int(put())
print(n - 2 if n > 2 else 1)