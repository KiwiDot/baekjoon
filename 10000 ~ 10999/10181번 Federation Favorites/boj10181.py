# 백준 10181번 Federation Favorites
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if n == -1:
        break

    d = [i for i in range(1, n//2+1) if not n % i]

    if n == sum(d):
        print("{} = {}".format(n, ' + '.join([str(i) for i in d])))
    else:
        print("{} is NOT perfect.".format(n))