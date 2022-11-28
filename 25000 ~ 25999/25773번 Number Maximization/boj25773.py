# 백준 25773번 Number Maximization
import sys
put = sys.stdin.readline

n = sorted(list(put().strip()), reverse=True)
print(''.join(n))