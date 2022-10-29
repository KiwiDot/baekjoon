# 백준 24084번 次の文字 (Next Character)
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

for i in range(N-1):
    if S[i+1] == 'J':
        print(S[i])