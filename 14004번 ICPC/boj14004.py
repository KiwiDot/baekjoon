# 백준 14004번 ICPC
import sys
put = sys.stdin.readline

A, B, C, D = map(int, put().split())
cnt = (C + D) // (A - B)

print(cnt)