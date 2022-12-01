# 백준 21945번 Palindromes
import sys
put = sys.stdin.readline

n = int(put())
num = put().split()
answer = 0

for i in num:
    if i == i[::-1]:
        answer += int(i)

print(answer)