# 백준 17250번 Balanced String
import sys
put = sys.stdin.readline

n = int(put())

print(2 ** ((n+1) // 2) % 16769023)