# 백준 14174번 Block Game
import sys
put = sys.stdin.readline

N = int(put())
alphabet = [0] * 26

for n in range(N):
    word1, word2 = put().split()
    w1, w2 = [0] * 26, [0] * 26

    for i in word1:
        w1[ord(i)-97] += 1
    for i in word2:
        w2[ord(i)-97] += 1

    for i in range(26):
        alphabet[i] += max(w1[i], w2[i])

for i in alphabet:
    print(i)