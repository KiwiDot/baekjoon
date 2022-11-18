# 백준 5602번 問題1
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
vote = {}
for i in range(m):
    vote[i+1] = 0

while n:
    n -= 1
    student = [int(_) for _ in put().split()]
    for i in range(m):
        if student[i]:
            vote[i+1] += 1

vote_ = sorted(vote.keys(), key=lambda x: vote[x], reverse=True)

for i in vote_:
    print(i, end=' ')
print()