# 백준 6783번 English or French?
import sys
put = sys.stdin.readline

N = int(put())
cnt_s = cnt_t = 0

while N:
    N -= 1
    text = put().strip().lower()

    cnt_s += text.count('s')
    cnt_t += text.count('t')

if cnt_t > cnt_s:
    print("English")
else:
    print("French")