# 백준 26736번 Wynik meczu
import sys
put = sys.stdin.readline

memo = put().strip()
X = memo.count('A')
Y = len(memo) - X

print("{} : {}".format(X, Y))