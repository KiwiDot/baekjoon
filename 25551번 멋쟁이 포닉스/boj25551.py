# 백준 25551번 멋쟁이 포닉스
import sys
put = sys.stdin.readline

Mw, Mb = map(int, put().split())
Tw, Tb = map(int, put().split())
Pw, Pb = map(int, put().split())

w = min(Mw, Tb, Pw)
b = min(Mb, Tw, Pb)

if w == b:
    print(min(w, b) * 2)

else:
    print(min(w, b) * 2 + 1)