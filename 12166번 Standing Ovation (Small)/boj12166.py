# 백준 12166번 Standing Ovation (Small)
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    Smax, S = put().split()
    cnt = friend = 0

    for k in range(int(Smax) + 1):
        if cnt < k:
            friend += 1
            cnt += int(S[k]) + 1
        else:
            cnt += int(S[k])

    print("Case #{}: {}".format(t, friend))