# 백준 17509번 And the Winner Is... Ourselves!
import sys
put = sys.stdin.readline

T = answer = 0
DV = sorted([[int(_) for _ in put().split()] for i in range(11)])

for i in DV:
    D, V = i
    T += D
    answer += T + V * 20

print(answer)
