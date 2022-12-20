# 백준 25966번 배찬우는 배열을 좋아해
import sys
put = sys.stdin.readline

N, M, q = map(int, put().split())
arr = [put().split() for i in range(N)]

while q:
    q -= 1
    query = put().split()

    if query[0] == '0':
        i, j, k = query[1:]
        arr[int(i)][int(j)] = k

    else:
        i, j = query[1:]
        i, j = int(i), int(j)
        arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(' '.join(i))