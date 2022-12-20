# 백준 5358번 Football Team
change = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'}

while True:
    try:
        name = list(input())
        for i in range(len(name)):
            if name[i] in change:
                name[i] = change[name[i]]

        print(''.join(name))

    except EOFError:
        break