# 백준 4606번 The Seven Percent Solution
import sys
put = sys.stdin.readline

char = {' ': "%20", '!': "%21", '$': "%24", '%': "%25",
        '(': "%28", ')': "%29", '*': "%2a"}
c = "% !$()*"

while True:
    s = put().strip()
    if s == '#':
        break

    for i in c:
        s = s.replace(i, char[i])

    print(s)
