# 백준 26040번 특정 대문자를 소문자로 바꾸기
import sys
put = sys.stdin.readline

A = put().strip()
B = put().split()

for i in B:
    A = A.replace(i, i.lower())

print(A)