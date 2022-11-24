# 백준 11760번 Mastering Mastermind
import sys
put = sys.stdin.readline

n, code, guess = put().split()
r, s = 0, []

for i in range(int(n)):
    if code[i] == guess[i]:
        r += 1

correct = list(set(code) & set(guess))
for i in correct:
    s += [i] * min(code.count(i), guess.count(i))

s = len(s) - r
print(r, s)