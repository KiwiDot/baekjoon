# 백준 26918번 Chronogram
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    chronogram = put().strip()
    answer = 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in letter.keys():
        answer += chronogram.count(i) * letter[i]

    print(answer)