# 백준 26307번 Correct
import sys
put = sys.stdin.readline

HH, MM = map(int, put().split())
answer = (HH - 9) * 60 + MM

print(answer)