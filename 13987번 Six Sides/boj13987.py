# 백준 13987번 Six Sides
import sys
put = sys.stdin.readline

dice1 = [int(_) for _ in put().split()]
dice2 = [int(_) for _ in put().split()]
win = lose = 0

for i in range(6):
    for j in range(6):
        if dice1[i] > dice2[j]:
            win += 1
        elif dice1[i] < dice2[j]:
            lose += 1

answer = win / (win + lose)
print("{:.5f}".format(answer))