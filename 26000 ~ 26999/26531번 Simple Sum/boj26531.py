# 백준 26531번 Simple Sum
import sys
put = sys.stdin.readline

a_b, c = put().split(' = ')

if eval(a_b) == int(c):
    print("YES")
else:
    print("NO")