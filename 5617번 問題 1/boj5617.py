# 백준 5617번 問題 1
cnt = [0, 0, 0, 0]  # 삼각형, 직각, 예각, 둔각

while True:
    try:
        a, b, c = sorted([int(_) for _ in input().split()])
        if a + b > c:
            cnt[0] += 1

            if a ** 2 + b ** 2 > c ** 2:
                cnt[2] += 1

            elif a ** 2 + b ** 2 < c ** 2:
                cnt[3] += 1

            else:
                cnt[1] += 1

        else:
            break

    except EOFError:
        break

print(' '.join([str(i) for i in cnt]))