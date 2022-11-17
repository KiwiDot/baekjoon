# 백준 13462번 Battle Simulation
import sys
put = sys.stdin.readline

monster = put().strip()
idx = 0

while idx != len(monster):
    if idx < len(monster) - 2:
        if {monster[idx], monster[idx+1], monster[idx+2]} == {'L', 'B', 'R'}:
            print('C', end='')
            idx += 3

        else:
            if monster[idx] == 'L':
                print('H', end='')
            elif monster[idx] == 'R':
                print('S', end='')
            else:
                print('K', end='')
            idx += 1

    else:
        if monster[idx] == 'L':
            print('H', end='')
        elif monster[idx] == 'R':
            print('S', end='')
        else:
            print('K', end='')
        idx += 1

print()