# 백준 4287번 Word Ratios
import sys
put = sys.stdin.readline

while True:
    word = put().split()
    if word == ['#']:
        break

    letter = []
    for i in range(len(word[0])):
        w = ord(word[1][i]) - ord(word[0][i])
        if w < 0:
            w += 26
        letter.append(w)

    w4 = ""
    for i in range(len(word[0])):
        w = ord(word[2][i]) + letter[i]
        if w > ord('z'):
            w -= 26
        w4 += chr(w)
    word.append(w4)

    print(' '.join(word))
