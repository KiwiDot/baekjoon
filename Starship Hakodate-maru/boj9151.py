# 백준 9151번 Starship Hakodate-maru
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    n1 = n2 = n3 = 0

    for i in range(int(n ** (1/3)), 55):
        if i ** 3 > n:
            break
        n1 = i

    for i in range(int(n ** (1/3)) // 6, 1000):
        if i * (i+1) * (i+2) / 6 > n:
            break
        n2 = i

    for i1 in range(n1+1):
        for i2 in range(n2+1):
            result = i1 ** 3 + i2 * (i2+1) * (i2+2) // 6
            if result > n:
                break

            n3 = max(n3, result)

    print(n3)