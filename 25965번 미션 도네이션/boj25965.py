# 백준 25965번 미션 도네이션
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    M = int(put())
    money = 0
    mission = []

    while M:
        M -= 1
        K, D, A = map(int, put().split())
        mission.append([K, D, A])

    k, d, a = map(int, put().split())
    for i in mission:
        K, D, A = i
        m = k * K - d * D + a * A
        if m > 0:
            money += m

    print(money)