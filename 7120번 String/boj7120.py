# 백준 7120번 String
import sys
put = sys.stdin.readline

text = put().strip()
string = text[0]

for i in text:
    if string[-1] == i:
        continue
    string += i

print(string)