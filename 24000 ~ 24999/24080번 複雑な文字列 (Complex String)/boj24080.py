# 백준 24080번 複雑な文字列 (Complex String)
import sys
put = sys.stdin.readline

N = int(put())
S = set(put().strip())

if len(S) >= 3:
    print("Yes")
else:
    print("No")
