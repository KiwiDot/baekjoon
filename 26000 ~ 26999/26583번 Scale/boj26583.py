# 백준 26583번 Scale

while True:
    try:
        num = [int(_) for _ in input().split()]
        n = num.copy()
        for i in range(len(n)):
            if not i:
                if len(n) > 1:
                    num[0] *= n[1]
            elif i == len(n) - 1:
                num[-1] *= n[-2]
            else:
                num[i] *= n[i-1] * n[i+1]

            print(num[i], end=' ')
        print()

    except EOFError:
        break
