# 백준 6976번 Divisibility by 11
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = put().strip()
    N = n

    while len(n) > 2:
        print(n)
        n_ = n[-1]
        n = str(int(n[:len(n)-1]) - int(n_))

    print(n)
    if int(n) % 11:
        print("The number {} is not divisible by 11.".format(N))
    else:
        print("The number {} is divisible by 11.".format(N))
    print()
