# 백준 6830번 It’s Cold Here!
import sys
put = sys.stdin.readline

canada = {}

while True:
    city, temperature = put().split()
    canada[city] = int(temperature)
    if city == "Waterloo":
        break

print(min(canada, key=canada.get))