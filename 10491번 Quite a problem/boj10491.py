# 백준 10491번 Quite a problem

while True:
    try:
        s = input().lower()
        if "problem" in s:
            print("yes")
        else:
            print("no")

    except EOFError:
        break