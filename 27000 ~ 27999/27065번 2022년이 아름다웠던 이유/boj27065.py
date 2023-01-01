# 백준 27065번 2022년이 아름다웠던 이유
import sys
put = sys.stdin.readline

T = int(put())
ba = set()     # 부족수 & 완전수
g = set()      # 과잉수

while T:
    T -= 1
    n = int(put())
    check = True
    div = [1]

    for i in range(2, int(n**0.5)+1):
        if not n % i:
            div.append(i)
            if i ** 2 != n:
                div.append(n // i)

    if n < sum(div) and not set(div) & g:
        for i in list(set(div) - ba):
            d = [j for j in range(1, i//2+1) if not i % j]
            if i < sum(d):
                g.add(i)
                check = False
                break
            else:
                ba.add(i)

    else:
        check = False

    if check:
        print("Good Bye")
    else:
        print("BOJ 2022")