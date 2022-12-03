# 백준 2891번 카약과 강풍
import sys
put = sys.stdin.readline

N, S, R = map(int, put().split())
s = [int(_) for _ in put().split()]
r = [int(_) for _ in put().split()]

# 카약을 여분을 준비한 팀이 손상되었을 경우, 빌려주지 않는다.
for i in r.copy():
    if i in s:
        s.remove(i)
        r.remove(i)

while s and r:
    r2 = []
    for i in r:
        # 앞뒤 팀 모두 카약이 없는 경우 - 순서를 나중으로 미룬다
        if i-1 in s and i+1 in s:
            r2.append(i)
        # 앞뒤 팀 중 한 팀만 카약이 없는 경우 - 카약을 무조건 준다.
        elif i-1 in s:
            s.remove(i-1)
        elif i+1 in s:
            s.remove(i+1)
        # 카약을 줄 수 있는 팀이 없는 경우
        else:
            r2.append(i)

    # 카약을 더이상 줄 수 없거나, 어느 팀한테 줘도 상관 없음
    if r == r2:
        break

    r = r2

for i in r:
    if i-1 in s:
        s.remove(i-1)
    elif i+1 in s:
        s.remove(i+1)

print(len(s))