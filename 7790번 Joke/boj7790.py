# 백준 7790번 Joke
cnt = 0

while True:
    try:
        text = input().strip()
        cnt += text.count("joke")

    except EOFError:
        break

print(cnt)
