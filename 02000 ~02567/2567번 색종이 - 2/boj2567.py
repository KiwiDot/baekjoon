# 백준 2567번 색종이 - 2
import sys
put = sys.stdin.readline

paper = [[0 for _ in range(102)] for i in range(102)]
n = int(put())
cnt = 0

while n:
    n -= 1
    x, y = map(int, put().split())
    for i in range(1, 11):
        for j in range(1, 11):
            paper[x+i][y+j] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j]:
            s = [paper[i-1][j], paper[i+1][j], paper[i][j-1], paper[i][j+1]]
            cnt += s.count(0)

print(cnt)