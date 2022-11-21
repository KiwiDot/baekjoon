# 백준 11605번 Magic Trick
import sys
put = sys.stdin.readline

n = int(put())
k = [int(i+1) for i in range(100)]

while n:
    n -= 1
    oprt, x = put().split()
    x = int(x)

    if oprt == "ADD":
        for i in range(100):
            if k[i] >= 0:
                k[i] += x

    elif oprt == "SUBTRACT":
        for i in range(100):
            if k[i] >= x:
                k[i] -= x
            else:
                k[i] = -1

    elif oprt == "MULTIPLY":
        for i in range(100):
            if k[i] >= 0:
                k[i] *= x

    else:
        for i in range(100):
            if k[i] >= 0 and k[i] % x == 0:
                k[i] //= x
            else:
                k[i] = -1

print(k.count(-1))