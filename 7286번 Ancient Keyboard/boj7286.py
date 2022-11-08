# 백준 7286번 Ancient Keyboard
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    tape = {}

    while n:
        n -= 1
        key, a, b = put().split()
        for i in range(int(a), int(b)):
            if i in tape:
                tape[i] += 1
            else:
                tape[i] = 1

    for i in sorted(tape.keys()):
        print(chr(tape[i] + 64), end='')
    print()