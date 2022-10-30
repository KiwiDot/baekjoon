# 백준 10643번 FUNGHI
import sys
put = sys.stdin.readline

mushroom = [int(put()) for i in range(8)]
mushroom += mushroom

pizza = [sum(mushroom[i:i+4]) for i in range(8)]

print(max(pizza))