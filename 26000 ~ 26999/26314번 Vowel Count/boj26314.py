# 백준 26314번 Vowel Count
import sys
put = sys.stdin.readline

n = int(put())
vowel = {'a', 'e', 'i', 'o', 'u'}

while n:
    n -= 1
    name = put().strip()
    cnt1 = cnt2 = 0

    for i in name:
        if i in vowel:
            cnt1 += 1
    cnt2 = len(name) - cnt1

    print(name)
    if cnt1 > cnt2:
        print(1)
    else:
        print(0)
