# 백준 11809번 YODA
import sys
put = sys.stdin.readline

N = put().strip()
M = put().strip()
length = max(len(N), len(M))

N = list(N.zfill(length))
M = list(M.zfill(length))

for i in range(length):
    n = int(N[i])
    m = int(M[i])

    if n > m:
        M[i] = ''
    elif n < m:
        N[i] = ''

n = ''.join(N)
m = ''.join(M)

print(int(n) if n else "YODA")
print(int(m) if m else "YODA")