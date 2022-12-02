# 백준 1064번 평행사변형
import sys
put = sys.stdin.readline

Xa, Ya, Xb, Yb, Xc, Yc = map(int, put().split())

# A, B, C 세 점이 모두 한 직선 상에 있는 경우 -> 평행사변형을 만들 수 없는 경우
if Xa == Xb == Xc == 0 or (Ya - Yb) * (Xa - Xc) == (Xa - Xb) * (Ya - Yc):
    print(-1)

else:
    ab = ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** 0.5
    bc = ((Xb - Xc) ** 2 + (Yb - Yc) ** 2) ** 0.5
    ca = ((Xc - Xa) ** 2 + (Yc - Ya) ** 2) ** 0.5

    print((max(ab, bc, ca) - min(ab, bc, ca)) * 2)