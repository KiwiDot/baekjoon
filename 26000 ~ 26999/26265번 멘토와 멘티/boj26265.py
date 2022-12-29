# 백준 26265번 멘토와 멘티
import sys
put = sys.stdin.readline

N = int(put())
tutoring = [put().split() for i in range(N)]

tutoring.sort(key=lambda x: x[1], reverse=True)
tutoring.sort(key=lambda x: x[0])

for i in tutoring:
    print(' '.join(i))