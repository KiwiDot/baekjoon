# 백준 26742번 Skarpetki
import sys
put = sys.stdin.readline

socks = put().strip()
b = socks.count('B')
c = len(socks) - b

print(b//2 + c//2)