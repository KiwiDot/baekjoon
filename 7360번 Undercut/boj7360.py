# 백준 7360번 Undercut
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    a, b = 0, 0

    A = [int(_) for _ in put().split()]
    B = [int(_) for _ in put().split()]

    for i in range(n):
        if A[i] == B[i]:
            continue

        elif abs(A[i] - B[i]) == 1:
            if A[i] + B[i] == 3:
                if A[i] < B[i]:
                    a += 6
                else:
                    b += 6

            else:
                if A[i] < B[i]:
                    a += A[i] + B[i]
                else:
                    b += A[i] + B[i]

        else:
            if A[i] > B[i]:
                a += A[i]
            else:
                b += B[i]

    print("A has {} points. B has {} points.".format(a, b))
    print()