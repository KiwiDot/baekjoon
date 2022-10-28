# 백준 25643번 문자열 탑 쌓기
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
S = put().strip()
check = True

for i in range(N-1):
    s = put().strip()
    check2 = False      # 탑을 쌓을 수 있다면 

    for m in range(1, M+1):
        if S[:m] == s[-m:] or S[-m:] == s[:m]:
            check2 = True
            break

    if check2:
        S = s
    else:
        check = False
        break

print(1 if check else 0)
