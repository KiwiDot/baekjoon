# 백준 9296번 Grading Exams
import sys

put = sys.stdin.readline

t = int(put())

for i in range(1, t + 1):
    t -= 1
    L = int(put())
    s1, s2 = put().strip(), put().strip()
    cnt = 0

    for l in range(L):
        if s1[l] != s2[l]:
            cnt += 1

    print("Case {}: {}".format(i, cnt))