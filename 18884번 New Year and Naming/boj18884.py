# 백준 18884번 New Year and Naming
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
s = put().split()
t = put().split()
q = int(put())

while q:
    q -= 1
    y = int(put()) - 1

    print(s[y % n] + t[y % m])