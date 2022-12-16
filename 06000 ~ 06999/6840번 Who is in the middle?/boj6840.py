# 백준 6840번 Who is in the middle?
import sys
put = sys.stdin.readline

bear = sorted([int(put()) for i in range(3)])
print(bear[1])