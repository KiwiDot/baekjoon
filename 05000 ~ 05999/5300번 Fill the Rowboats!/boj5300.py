# 백준 5300번 Fill the Rowboats!
import sys
put = sys.stdin.readline

N = int(put())

for i in range(1, N+1):
    print(i, end=' ')
    if i == N or not i % 6:
        print("Go!", end=' ')