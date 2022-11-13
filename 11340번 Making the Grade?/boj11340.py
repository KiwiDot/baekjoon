# 백준 11340번 Making the Grade?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    score = [int(_) for _ in put().split()]

    # 15% / 20% / 25% 이므로 20을 곱해주면 깔끔하게 300% / 400% / 500%가 된다
    cnt = score[0] * 3 + score[1] * 4 + score[2] * 5

    if cnt < 1000:
        print("impossible")

    else:
        s = 1800 - cnt
        print(s // 8 + 1 if s % 8 else s // 8)
