# 백준 20959번 Šifra
import sys
put = sys.stdin.readline

word = put().strip()

for i in range(26):
    word = word.replace(chr(i+97), ' ')

print(len(set(word.split())))