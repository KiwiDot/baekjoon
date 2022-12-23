# 백준 26731번 Zagubiona litera
import sys
put = sys.stdin.readline

answer = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - set(put())
print(list(answer)[0])