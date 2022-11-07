# 백준 9884번 Euclid
import sys
import math
put = sys.stdin.readline

n1, n2 = map(int, put().split())
gcd = math.gcd(n1, n2)

print(gcd)