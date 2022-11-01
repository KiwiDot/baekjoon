# 백준 18141번 Are They All Integers?
import sys
put = sys.stdin.readline

n = int(put())
A = sorted([int(_) for _ in put().split()])

if A == A[0] * len(A):
    print("yes")

elif (A[-1] / A[0]).is_integer() and A == [A[0]] * (len(A)-1) + [A[-1]]:
    print("yes")

else:
    print("no")