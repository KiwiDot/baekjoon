# 백준 6565번 Hard to Believe, but True!
import sys
put = sys.stdin.readline

while True:
    result, equation = put().strip()[::-1].split('=')
    if result == '0' and equation == '0+0':
        print(True)
        break

    result = int(result)
    e1, e2 = equation.split('+')
    equation = int(e1) + int(e2)

    print(result == equation)