# 백준 16360번 Go Latin
import sys
put = sys.stdin.readline

Latin = {'a': 'as', 'i': 'ios', 'y': 'ios', 'l': 'les',
         'n': 'anes', 'ne': 'anes', 'o': 'os', 'r': 'res',
         't': 'tas', 'u': 'us', 'v': 'ves', 'w': 'was'}

n = int(put())

while n:
    n -= 1
    word = put().strip()
    check = True

    for i in Latin.keys():
        if word.endswith(i):
            word = word[:-len(i)] + Latin[i]
            check = False
            break

    if check:
        word += "us"

    print(word)