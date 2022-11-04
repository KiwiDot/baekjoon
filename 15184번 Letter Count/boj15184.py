# 백준 15184번 Letter Count
import sys
put = sys.stdin.readline

s = put().strip().upper()
alphabet = [""] * 26

for i in s:
    if i.isalpha():
        alphabet[ord(i)-65] += '*'

for i in range(26):
    print("{} | {}".format(chr(i+65), alphabet[i]))