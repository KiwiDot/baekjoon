# 백준 17285번 XORChic
import sys
put = sys.stdin.readline

T = put().strip()
t = ""

key = ord(T[0]) ^ ord('C')
for i in T:
    t += chr(ord(i) ^ key)

print(t)