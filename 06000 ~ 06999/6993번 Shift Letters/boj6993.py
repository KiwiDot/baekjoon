# 백준 6993번 Shift Letters
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    w, n = put().split()
    n = int(n)

    print("Shifting {} by {} positions gives us: {}".format(w, n, w[-n:] + w[:-n]))
