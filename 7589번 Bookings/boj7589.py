# 백준 7589번 Bookings
import sys
put = sys.stdin.readline

while True:
    num, n = put().split()
    if num == '#' and n == '0':
        break
    n = int(n)

    while True:
        data = put().split()
        if data == ['X', '0']:
            break

        if data[0] == 'B' and n + int(data[1]) <= 68:
            n += int(data[1])

        elif data[0] == 'C' and n >= int(data[1]):
            n -= int(data[1])

    print(num, n)