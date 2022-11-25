# 백준 20978번 共通要素 (Common Elements)
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = set([int(_) for _ in put().split()])
B = set([int(_) for _ in put().split()])

for i in sorted(list(A & B)):
    print(i)